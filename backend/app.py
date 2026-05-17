import re
from base64 import b64decode
from io import BytesIO
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import joblib

try:
    import pytesseract
except ImportError:  # pragma: no cover
    pytesseract = None

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from PIL import Image
from sklearn.pipeline import Pipeline


MODEL_PATH = Path(__file__).resolve().parent / "model.pkl"
ROOT_MODEL_PATH = Path(__file__).resolve().parent.parent / "model.pkl"
MAX_REVIEW_SAMPLES = 15
SPAMMY_PATTERNS = [
    r"!{2,}",
    r"best product ever",
    r"must buy",
    r"highly recommend",
    r"life changing",
    r"you need this",
    r"order now",
    r"buy now",
    r"unrealistic",
    r"limited time",
    r"special offer",
    r"amazing deal",
    r"don't miss",
    r"best.*ever",
    r"love (it|this|them)",
    r"perfect(ly)?",
    r"5 stars?",
    r"10/10",
    r"so good",
    r"too good to be true",
]


class TextRequest(BaseModel):
    """Payload for plain text review analysis."""
    text: str


class PredictRequest(BaseModel):
    """Unified payload for the /predict endpoint."""
    mode: Optional[str] = "text"
    review: Optional[str] = None
    image_base64: Optional[str] = None


app = FastAPI(
    title="AI Review Analyzer",
    description="A FastAPI backend for analyzing reviews from text or screenshots.",
    version="1.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def find_model_path() -> Path:
    if MODEL_PATH.exists():
        return MODEL_PATH
    if ROOT_MODEL_PATH.exists():
        return ROOT_MODEL_PATH
    return MODEL_PATH


def load_saved_model(model_path: Path) -> Tuple[Pipeline, float]:
    """Load the trained model pipeline and saved score from disk."""
    if not model_path.exists():
        raise FileNotFoundError(
            f"Model file not found at {model_path}. Run backend/train.py first to train and save the model."
        )

    try:
        model_data = joblib.load(model_path)
    except Exception:
        # Fallback to pickle for backward compatibility
        import pickle
        with model_path.open("rb") as file:
            model_data = pickle.load(file)

    score = float(model_data.get("test_score", model_data.get("score", 0.0)))
    return model_data["pipeline"], score


def extract_reviews_from_image(file_bytes: bytes) -> List[str]:
    """Use OCR to extract review text from an uploaded screenshot image."""
    if pytesseract is None:
        raise RuntimeError(
            "OCR support is not available because pytesseract is not installed. "
            "Install pytesseract and Tesseract OCR to enable screenshot analysis."
        )

    image = Image.open(BytesIO(file_bytes))
    raw_text = pytesseract.image_to_string(image, lang="eng")
    lines = [line.strip() for line in raw_text.splitlines() if len(line.strip()) > 30]

    if not lines:
        raw_text = raw_text.strip()
        if raw_text:
            lines = [raw_text]

    return lines[:MAX_REVIEW_SAMPLES]


def decode_base64_image(image_base64: str) -> bytes:
    """Decode a Base64 image string and return raw bytes."""
    if "," in image_base64:
        image_base64 = image_base64.split(",", 1)[1]
    try:
        return b64decode(image_base64)
    except Exception as exc:
        raise ValueError(f"Invalid image data: {exc}")


def clean_text(text: str) -> str:
    text = str(text or "").strip()
    text = re.sub(r"\s+", " ", text)
    return text


def score_spammy_patterns(text: str) -> Dict[str, object]:
    score = 0
    matches = []
    normalized = text.lower()

    for pattern in SPAMMY_PATTERNS:
        if re.search(pattern, normalized):
            score += 1
            matches.append(pattern)

    repeated_phrases = len(re.findall(r"(love|great|best|perfect|amazing|recommend)\b", normalized))
    if repeated_phrases >= 3:
        score += 1
        matches.append("repeated praise")

    return {"spam_score": score, "patterns": sorted(set(matches))}


def adjust_prediction(prediction: str, confidence: float, text: str) -> Tuple[str, float, Dict[str, object]]:
    details = score_spammy_patterns(text)
    if details["spam_score"] >= 2 and prediction == "genuine":
        return "fake", max(confidence, 85.0), details
    return prediction, confidence, details


def normalize_prediction(raw_prediction: object) -> str:
    value = str(raw_prediction).strip().lower()
    if value in {"fake", "genuine"}:
        return value
    if value == "cg":
        return "genuine"
    if value == "or":
        return "fake"
    return "genuine" if "g" in value else "fake"


def predict_text(model: Pipeline, text: str) -> Tuple[str, float, Dict[str, object]]:
    """Predict whether the provided review text is genuine or fake."""
    cleaned = clean_text(text)
    raw_prediction = model.predict([cleaned])[0]
    probabilities = model.predict_proba([cleaned])[0]
    normalized_prediction = normalize_prediction(raw_prediction)
    confidence = round(float(max(probabilities)) * 100.0, 2)
    return adjust_prediction(normalized_prediction, confidence, cleaned)


def summarize_results(results: List[Tuple[str, float, Dict[str, object]]]) -> Dict[str, object]:
    """Summarize model predictions into fake percentage and trust score."""
    total_reviews = len(results)
    if total_reviews == 0:
        return {"review_count": 0, "fake_percentage": 0.0, "trust_score": 0.0, "average_confidence": 0.0}
    fake_count = sum(1 for prediction, _, _ in results if prediction == "fake")
    average_confidence = round(sum(confidence for _, confidence, _ in results) / total_reviews, 2)
    fake_percentage = round((fake_count / total_reviews) * 100.0, 2)
    trust_score = round(((100.0 - fake_percentage) * (average_confidence / 100.0)), 2)

    return {
        "review_count": total_reviews,
        "fake_percentage": fake_percentage,
        "trust_score": trust_score,
        "average_confidence": average_confidence,
    }


@app.on_event("startup")
async def startup_event() -> None:
    model, score = load_saved_model(find_model_path())
    app.state.model = model
    app.state.training_score = round(score * 100.0, 2)


@app.get("/")
async def read_root() -> Dict[str, str]:
    return {
        "message": "AI Review Analyzer backend is running.",
        "info": "Use /analyze/text or /analyze/screenshot to submit data.",
    }


@app.post("/analyze/text")
async def analyze_text(request: TextRequest) -> Dict[str, object]:
    text = request.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Please provide non-empty review text.")

    model: Pipeline = app.state.model
    prediction, confidence, pattern_details = predict_text(model, text)
    fake_percentage = 100.0 if prediction == "fake" else 0.0
    trust_score = round(confidence if prediction == "genuine" else 100.0 - confidence, 2)

    return {
        "analysis_type": "Text Review",
        "prediction": prediction,
        "confidence": confidence,
        "fake_percentage": fake_percentage,
        "trust_score": trust_score,
        "training_score": app.state.training_score,
        "review_count": 1,
        "review_text": text,
        "pattern_insights": pattern_details,
        "sample_reviews": [
            {"text": text, "prediction": prediction, "confidence": confidence, "patterns": pattern_details}
        ],
    }


@app.post("/analyze/screenshot")
async def analyze_screenshot(file: UploadFile = File(...)) -> Dict[str, object]:
    if not file.filename:
        raise HTTPException(status_code=400, detail="Please upload a screenshot image file.")
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Uploaded file must be an image.")

    file_bytes = await file.read()
    try:
        reviews = extract_reviews_from_image(file_bytes)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"OCR processing failed: {exc}")

    if not reviews:
        raise HTTPException(status_code=422, detail="No readable review text was detected in the uploaded screenshot.")

    model: Pipeline = app.state.model
    results = [predict_text(model, review) for review in reviews]
    summary = summarize_results(results)

    return {
        "analysis_type": "Screenshot OCR",
        "fake_percentage": summary["fake_percentage"],
        "trust_score": summary["trust_score"],
        "confidence": summary["average_confidence"],
        "training_score": app.state.training_score,
        "review_count": summary["review_count"],
        "extracted_text": "\n\n".join(reviews),
        "sample_reviews": [
            {
                "text": reviews[i],
                "prediction": results[i][0],
                "confidence": results[i][1],
                "patterns": results[i][2],
            }
            for i in range(min(len(reviews), 5))
        ],
    }


@app.post("/predict")
async def predict(request: PredictRequest) -> Dict[str, object]:
    mode = (request.mode or "text").lower()
    model: Pipeline = app.state.model

    if mode == "text":
        review = (request.review or "").strip()
        if not review:
            raise HTTPException(status_code=400, detail="Please provide review text for analysis.")

        prediction, confidence, pattern_details = predict_text(model, review)
        return {
            "analysis_type": "Text Review",
            "prediction": prediction,
            "confidence": confidence,
            "fake_percentage": 100.0 if prediction == "fake" else 0.0,
            "trust_score": round(confidence if prediction == "genuine" else 100.0 - confidence, 2),
            "training_score": app.state.training_score,
            "review_count": 1,
            "review_text": review,
            "pattern_insights": pattern_details,
            "sample_reviews": [
                {"text": review, "prediction": prediction, "confidence": confidence, "patterns": pattern_details}
            ],
        }

    if mode == "screenshot":
        image_base64 = (request.image_base64 or "").strip()
        if not image_base64:
            raise HTTPException(status_code=400, detail="Please provide screenshot image data for analysis.")

        try:
            file_bytes = decode_base64_image(image_base64)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc))

        try:
            reviews = extract_reviews_from_image(file_bytes)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=f"OCR processing failed: {exc}")

        if not reviews:
            raise HTTPException(status_code=422, detail="No readable review text was detected in the uploaded screenshot.")

        results = [predict_text(model, review) for review in reviews]
        summary = summarize_results(results)

        return {
            "analysis_type": "Screenshot OCR",
            "fake_percentage": summary["fake_percentage"],
            "trust_score": summary["trust_score"],
            "confidence": summary["average_confidence"],
            "training_score": app.state.training_score,
            "review_count": summary["review_count"],
            "extracted_text": "\n\n".join(reviews),
            "sample_reviews": [
                {
                    "text": reviews[i],
                    "prediction": results[i][0],
                    "confidence": results[i][1],
                    "patterns": results[i][2],
                }
                for i in range(min(len(reviews), 5))
            ],
        }

    raise HTTPException(status_code=400, detail="Unsupported analysis mode. Use text or screenshot.")
