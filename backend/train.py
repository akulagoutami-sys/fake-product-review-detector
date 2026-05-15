import pickle
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


DATA_PATH = Path(__file__).resolve().parent.parent / "dataset" / "reviews.csv"
MODEL_PATH = Path(__file__).resolve().parent / "model.pkl"


def load_dataset(csv_path: Path):
    """Load review text and labels from a CSV file using pandas."""
    data = pd.read_csv(csv_path)
    data = data.dropna(subset=["review", "label"])
    reviews = data["review"].astype(str).tolist()
    labels = data["label"].astype(str).tolist()
    return reviews, labels


def build_training_pipeline():
    """Build a scikit-learn pipeline using TF-IDF and Logistic Regression."""
    pipeline = Pipeline(
        [
            (
                "vectorizer",
                TfidfVectorizer(stop_words="english", ngram_range=(1, 2), max_features=5000),
            ),
            ("classifier", LogisticRegression(solver="liblinear", random_state=42, max_iter=1000)),
        ]
    )
    return pipeline


def train_model(reviews, labels):
    """Train the model and return the fitted pipeline and accuracy score."""
    X_train, X_test, y_train, y_test = train_test_split(
        reviews, labels, test_size=0.2, random_state=42, stratify=labels
    )

    pipeline = build_training_pipeline()
    pipeline.fit(X_train, y_train)

    score = pipeline.score(X_test, y_test)
    return pipeline, round(float(score), 3)


def save_model(pipeline, score, model_path: Path):
    """Save the trained pipeline and score using pickle."""
    model_data = {"pipeline": pipeline, "score": score}
    with model_path.open("wb") as file:
        pickle.dump(model_data, file)


def main():
    reviews, labels = load_dataset(DATA_PATH)
    pipeline, score = train_model(reviews, labels)
    save_model(pipeline, score, MODEL_PATH)
    print(f"Model trained and saved to {MODEL_PATH}")
    print(f"Validation accuracy: {score}")


if __name__ == "__main__":
    main()
