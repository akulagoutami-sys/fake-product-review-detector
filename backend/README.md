# AI Review Analyzer Backend

This backend uses FastAPI to expose a modern review analysis API for text reviews, product links, and screenshot OCR.

## Files

- `app.py`: Main FastAPI server.
  - Loads a trained model from `backend/model.pkl`.
  - Supports `/analyze/text`, `/analyze/link`, and `/analyze/screenshot` endpoints.
- `train.py`: Reads the CSV dataset and trains the model.
- `requirements.txt`: Python dependencies needed to run and train the backend.

## Run the backend

1. Install dependencies:

```bash
pip install -r backend/requirements.txt
```

2. Train the model first:

```bash
python backend/train.py
```

3. Start the server:

```bash
uvicorn backend.app:app --reload --host 0.0.0.0 --port 8000
```

4. Use the API endpoints:

- `GET /`: Health check and status.
- `POST /analyze/text`: Analyze single text review.
- `POST /analyze/link`: Submit a product URL and scrape review text.
- `POST /analyze/screenshot`: Upload a screenshot image for OCR review extraction.

## Example

Text review request:

```bash
curl -X POST "http://127.0.0.1:8000/analyze/text" -H "Content-Type: application/json" -d '{"text": "I loved this product"}'
```

Screenshot request:

```bash
curl -X POST "http://127.0.0.1:8000/analyze/screenshot" -F "file=@review.png"
```

The backend is designed to be beginner-friendly with added comments and multi-input review analysis support.
