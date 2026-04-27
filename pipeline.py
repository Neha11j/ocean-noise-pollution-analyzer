#Updated By Satyam
# pipeline.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
import os

def run_pipeline():
    print("Step 1: Loading dataset...")
    df = pd.read_csv("sonar_acoustic_dataset.csv")

    print("Step 2: Preprocessing...")
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    # Encode labels
    le = LabelEncoder()
    y = le.fit_transform(y)

    # Scale features
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    print("Step 3: Train-test split...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Step 4: Training model...")
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    print("Step 5: Evaluation...")
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average="weighted")

    print(f"Accuracy: {acc}")
    print(f"F1 Score: {f1}")

    print("Step 6: Updating leaderboard...")
    leaderboard_path = "leaderboard/leaderboard.csv"

    if os.path.exists(leaderboard_path):
        lb = pd.read_csv(leaderboard_path)
    else:
        lb = pd.DataFrame(columns=["Model", "Accuracy", "F1 Score"])

    new_entry = pd.DataFrame({
        "Model": ["Random Forest"],
        "Accuracy": [acc],
        "F1 Score": [f1]
    })

    lb = pd.concat([lb, new_entry], ignore_index=True)
    lb = lb.sort_values(by="Accuracy", ascending=False)

    lb.to_csv(leaderboard_path, index=False)

    print("Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()
