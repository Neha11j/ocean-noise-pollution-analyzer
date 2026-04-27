"""
evaluate_and_log.py

Runs model evaluation and appends results to the leaderboard CSV.

Usage:
    python scripts/evaluate_and_log.py \
        --pr PR-42 \
        --branch feature/xgboost \
        --author alice \
        --note "Tuned XGBoost params" \
        --leaderboard leaderboard.csv
"""

import argparse
import csv
import os
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Replace this section with your actual model loading + evaluation logic
# ---------------------------------------------------------------------------
def run_evaluation() -> list[dict]:
    """
    Load your model(s) and test data, run evaluation, return a list of result dicts.

    Each dict must have these keys:
        model, accuracy, precision, recall, f1, auc

    Example using scikit-learn:

        from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
        import joblib, numpy as np

        model = joblib.load("models/latest.pkl")
        X_test = np.load("data/X_test.npy")
        y_test = np.load("data/y_test.npy")

        y_pred  = model.predict(X_test)
        y_proba = model.predict_proba(X_test)[:, 1]

        return [{
            "model": "MyModel",
            "accuracy":  round(accuracy_score(y_test, y_pred),       6),
            "precision": round(precision_score(y_test, y_pred, average="weighted"), 6),
            "recall":    round(recall_score(y_test, y_pred, average="weighted"),    6),
            "f1":        round(f1_score(y_test, y_pred, average="weighted"),        6),
            "auc":       round(roc_auc_score(y_test, y_proba),        6),
        }]
    """
    raise NotImplementedError(
        "Replace run_evaluation() with your actual model evaluation code."
    )
# ---------------------------------------------------------------------------


LEADERBOARD_HEADER = [
    "Model", "Accuracy", "Precision", "Recall", "F1 Score", "AUC",
    "PR", "Branch", "Author", "Note",
]


def append_to_leaderboard(
    leaderboard_path: str,
    results: list[dict],
    pr: str,
    branch: str,
    author: str,
    note: str,
) -> None:
    path = Path(leaderboard_path)
    write_header = not path.exists() or path.stat().st_size == 0

    with open(path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=LEADERBOARD_HEADER)

        if write_header:
            writer.writeheader()

        for r in results:
            writer.writerow({
                "Model":     r["model"],
                "Accuracy":  r.get("accuracy", ""),
                "Precision": r.get("precision", ""),
                "Recall":    r.get("recall", ""),
                "F1 Score":  r.get("f1", ""),
                "AUC":       r.get("auc", ""),
                "PR":        pr,
                "Branch":    branch,
                "Author":    author,
                "Note":      note,
            })

    print(f"[leaderboard] Appended {len(results)} row(s) to {path}")
    for r in results:
        print(
            f"  {r['model']}: "
            f"acc={r.get('accuracy','')} "
            f"f1={r.get('f1','')} "
            f"auc={r.get('auc','')}"
        )


def main():
    parser = argparse.ArgumentParser(description="Evaluate models and update leaderboard.")
    parser.add_argument("--pr",          required=True,  help="PR identifier, e.g. PR-42")
    parser.add_argument("--branch",      required=True,  help="Source branch name")
    parser.add_argument("--author",      required=True,  help="PR author / GitHub username")
    parser.add_argument("--note",        default="",     help="Short description / PR title")
    parser.add_argument("--leaderboard", default="leaderboard.csv", help="Path to leaderboard CSV")
    args = parser.parse_args()

    print(f"[leaderboard] Running evaluation for {args.pr} ({args.branch}) by {args.author}")
    results = run_evaluation()

    append_to_leaderboard(
        leaderboard_path=args.leaderboard,
        results=results,
        pr=args.pr,
        branch=args.branch,
        author=args.author,
        note=args.note,
    )


if __name__ == "__main__":
    main()
