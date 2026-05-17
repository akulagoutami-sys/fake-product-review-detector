"""
Train and save a fake review detector model using TF-IDF and Logistic Regression.
Supports Kaggle Fake Reviews Dataset with CG (fake) and OR (genuine) labels.
"""

import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    dataset_path = repo_root / "dataset" / "reviews.csv"
    model_path = repo_root / "model.pkl"

    df = pd.read_csv(dataset_path)

    print("Before conversion:")
    print(df["label"].value_counts())

    df["label"] = df["label"].replace({
        "CG": "fake",
        "OR": "genuine"
    })

    print("After conversion:")
    print(df["label"].value_counts())

    df = df.dropna()

    if "text" not in df.columns and "text_" in df.columns:
        df = df.rename(columns={"text_": "text"})

    X = df["text"]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(stop_words="english", ngram_range=(1,2))),
        ("clf", LogisticRegression(
            class_weight="balanced",
            max_iter=1000
        ))
    ])

    pipeline.fit(X_train, y_train)

    pred = pipeline.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, pred))
    print(confusion_matrix(y_test, pred))
    print(classification_report(y_test, pred))

    joblib.dump(pipeline, model_path)
    print("Model saved successfully")


if __name__ == "__main__":
    main()
