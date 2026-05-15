from base64 import b64decode
from io import BytesIO
from pathlib import Path
import pickle
from typing import Dict, List, Optional, Tuple

import httpx
import pytesseract
from bs4 import BeautifulSoup
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


class LinkRequest(BaseModel):
    """Payload for product link or URL analysis."""
    url: str


class PredictRequest(BaseModel):
    """Unified payload for the /predict endpoint."""
    mode: Optional[str] = "text"
    review: Optional[str] = None
    url: Optional[str] = None
    image_base64: Optional[str] = None


app = FastAPI(
    title="AI Review Analyzer",
    description="A FastAPI backend for analyzing reviews from text, product links, or screenshots.",
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
    """Load the trained model pipeline and the saved accuracy score."""
    if not model_path.exists():
        raise FileNotFoundError(
            f"Model file not found at {model_path}. Run backend/train.py first to train and save the model."
        )

    with model_path.open("rb") as file:
        model_data = pickle.load(file)

    return model_data["pipeline"], float(model_data.get("score", 0.0))


def extract_reviews_from_html(html: str) -> List[str]:
    """Extract review text from a product page using common HTML review selectors."""
    soup = BeautifulSoup(html, "html.parser")
    selectors = [
        "div.review",
        ".review-text",
        ".customer-review",
        ".review-body",
        ".review-content",
        ".review-item",
        ".comment",
        ".testimonial",
        ".feedback",
        "p",
    ]

    reviews: List[str] = []
    for selector in selectors:
        for element in soup.select(selector):
            text = element.get_text(separator=" ", strip=True)
            if len(text) > 30:
                reviews.append(text)

    cleaned_reviews: List[str] = []
    for review_text in reviews:
        if review_text not in cleaned_reviews:
            cleaned_reviews.append(review_text)
        if len(cleaned_reviews) >= MAX_REVIEW_SAMPLES:
            break

    if not cleaned_reviews:
        full_text = soup.get_text(separator="\n")
        lines = [line.strip() for line in full_text.splitlines() if len(line.strip()) > 80]
        cleaned_reviews = lines[:MAX_REVIEW_SAMPLES]

    return cleaned_reviews


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
    """Predict whether the text is genuine or fake and return confidence percent."""
    prediction = model.predict([text])[0]
    probabilities = model.predict_proba([text])[0]
    confidence = round(float(max(probabilities)) * 100.0, 2)
    return prediction, confidence


def summarize_results(results: List[Tuple[str, float]]) -> Dict[str, object]:
    """Compute fake percentage and trust score from prediction results."""
    total_reviews = len(results)
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
    """Load the saved model once when the server starts."""
    model, score = load_saved_model(MODEL_PATH)
    app.state.model = model
    app.state.training_score = round(score * 100.0, 2)


@app.get("/")
async def read_root() -> Dict[str, str]:
    """Health check endpoint for the API."""
    return {
        "message": "AI Review Analyzer backend is running.",
        "info": "Use /analyze/text, /analyze/link, or /analyze/screenshot to submit data.",
    }


@app.post("/analyze/text")
async def analyze_text(request: TextRequest) -> Dict[str, object]:
    """Analyze a single text review."""
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


@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()
    if not url:
        raise HTTPException(status_code=400, detail="Please provide a valid product URL.")

    async with httpx.AsyncClient(timeout=15.0, follow_redirects=True) as client:
        response = await client.get(url, headers={"User-Agent": "AI Review Analyzer/1.0"})

    if response.status_code >= 400:
        raise HTTPException(status_code=502, detail=f"Unable to fetch URL. HTTP {response.status_code}.")

    reviews = extract_reviews_from_html(response.text)
    if not reviews:
        raise HTTPException(status_code=404, detail="No review text could be extracted from the product page.")

    model: Pipeline = app.state.model
    results = [predict_text(model, review) for review in reviews]
    summary = summarize_results(results)

    return {
        "analysis_type": "Product Link",
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


@app.post("/analyze/screenshot")
async def analyze_screenshot(file: UploadFile = File(...)) -> Dict[str, object]:
    """Analyze reviews from a screenshot using OCR."""
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
    """Unified analyzer endpoint for text, link, and screenshot modes."""
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
            "trust_score": 100.0 - confidence * 100.0,
            "training_score": app.state.training_score,
            "review_count": 1,
            "sample_reviews": [{"text": review, "prediction": prediction, "confidence": confidence}],
            "review_text": review,
        }

    if mode == "link":
        url = (request.url or "").strip()
        if not url:
            raise HTTPException(status_code=400, detail="Please provide a valid product URL.")

        async with httpx.AsyncClient(timeout=15.0, follow_redirects=True) as client:
            response = await client.get(url, headers={"User-Agent": "AI Review Analyzer/1.0"})

        if response.status_code >= 400:
            raise HTTPException(status_code=502, detail=f"Unable to fetch URL. HTTP {response.status_code}.")

        reviews = extract_reviews_from_html(response.text)
        if not reviews:
            raise HTTPException(status_code=404, detail="No review text could be extracted from the product page.")

        results = [predict_text(model, review) for review in reviews]
        summary = summarize_results(results)

        return {
            "analysis_type": "Product Link",
            "fake_percentage": summary["fake_percentage"],
            "trust_score": summary["trust_score"],
            "confidence": summary["average_confidence"],
            "training_score": app.state.training_score,
            "review_count": summary["review_count"],
            "sample_reviews": [
                {"text": reviews[i], "prediction": results[i][0], "confidence": results[i][1]}
                for i in range(min(len(reviews), 5))
            ],
            "url": url,
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
            "extracted_text": reviews[0],
        }

    raise HTTPException(status_code=400, detail="Unsupported analysis mode. Use text, link, or screenshot.")
