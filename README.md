# fake-production-review-detector
AI-based system to detect fake and genuine product reviews using NLP and Machine Learning.

## Backend

The backend is implemented using FastAPI and is located in the `backend/` folder.

- `backend/app.py`: FastAPI server with the prediction endpoint and model loader.
- `backend/train.py`: Training script that loads the dataset, trains the model, and saves it with pickle.
- `backend/requirements.txt`: Python dependencies for the backend and training pipeline.
- `backend/README.md`: Instructions for training the model and running the backend.
- `dataset/reviews.csv`: Review dataset used to train the fake/genuine classifier.

## Frontend

A futuristic cyberpunk-themed AI dashboard available in the `frontend/` folder with neon UI, glassmorphism, animated backgrounds, and advanced visualizations.

- `frontend/index.html`: Cyberpunk dashboard with prediction meter, confidence bar, and animated elements
- `frontend/styles.css`: CSS with neon colors, glowing effects, moving gradients, and responsive design
- `frontend/script.js`: JavaScript for API integration, meter animations, and real-time stats
- `frontend/README.md`: Instructions for the futuristic frontend interface
