from base64 import b64decode
from io import BytesIO
from pathlib import Path
import pickle
from typing import Dict, List, Optional, Tuple

import pytesseract
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from PIL import Image
from sklearn.pipeline import Pipeline


MODEL_PATH = Path(__file__).resolve().parent / "model.pkl"
MAX_REVIEW_SAMPLES = 15


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


def load_saved_model(model_path: Path) -> Tuple[Pipeline, float]:
    """Load the trained model pipeline and saved score from disk."""
    if not model_path.exists():
        raise FileNotFoundError(
            f"Model file not found at {model_path}. Run backend/train.py first to train and save the model."
        )

    with model_path.open("rb") as file:
        model_data = pickle.load(file)

    return model_data["pipeline"], float(model_data.get("score", 0.0))


def extract_reviews_from_image(file_bytes: bytes) -> List[str]:
    """Use OCR to extract review text from an uploaded screenshot image."""
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


def predict_text(model: Pipeline, text: str) -> Tuple[str, float]:
    """Predict whether the provided review text is genuine or fake."""
    prediction = model.predict([text])[0]
    probabilities = model.predict_proba([text])[0]
    confidence = round(float(max(probabilities)) * 100.0, 2)
    return prediction, confidence


def summarize_results(results: List[Tuple[str, float]]) -> Dict[str, object]:
    """Summarize model predictions into fake percentage and trust score."""
    total_reviews = len(results)
    if total_reviews == 0:
        return {"review_count": 0, "fake_percentage": 0.0, "trust_score": 0.0, "average_confidence": 0.0}
    fake_count = sum(1 for prediction, _ in results if prediction == "fake")
    fake_percentage = round((fake_count / total_reviews) * 100.0, 2)
    average_confidence = round(sum(confidence for _, confidence in results) / total_reviews, 2)
    trust_score = round(((100.0 - fake_percentage) * (average_confidence / 100.0)), 2)

    return {
        "review_count": total_reviews,
        "fake_percentage": fake_percentage,
        "trust_score": trust_score,
        "average_confidence": average_confidence,
    }


@app.on_event("startup")
async def startup_event() -> None:
    model, score = load_saved_model(MODEL_PATH)
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
    prediction, confidence = predict_text(model, text)
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
        "sample_reviews": [
            {"text": text, "prediction": prediction, "confidence": confidence}
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
        "sample_reviews": [
            {"text": reviews[i], "prediction": results[i][0], "confidence": results[i][1]}
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

        prediction, confidence = predict_text(model, review)
        return {
            "analysis_type": "Text Review",
            "prediction": prediction,
            "confidence": confidence,
            "fake_percentage": 100.0 if prediction == "fake" else 0.0,
            "trust_score": round(confidence if prediction == "genuine" else 100.0 - confidence, 2),
            "training_score": app.state.training_score,
            "review_count": 1,
            "sample_reviews": [{"text": review, "prediction": prediction, "confidence": confidence}],
            "review_text": review,
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
            "sample_reviews": [
                {"text": reviews[i], "prediction": results[i][0], "confidence": results[i][1]}
                for i in range(min(len(reviews), 5))
            ],
        }

    raise HTTPException(status_code=400, detail="Unsupported analysis mode. Use text or screenshot.")
