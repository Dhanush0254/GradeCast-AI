import os
from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.pipeline import Pipeline

app = Flask(__name__)

# ---------- 1. LOAD DATA & TRAIN MODELS ON STARTUP ----------

# FIXED PATH: Uses relative path so it works on Cloud/GitHub
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'student_results.csv')

# Load Data
df = pd.read_csv(DATA_PATH)

# Features we'll use
feature_cols = ["hours_studied", "attendance", "previous_score", "assignments_completed"]

X = df[feature_cols]
y_class = df["passed"]        # for Pass/Fail (classification)
y_reg = df["final_score"]     # for marks prediction (regression)

X_train, X_test, y_class_train, y_class_test, y_reg_train, y_reg_test = train_test_split(
    X, y_class, y_reg, test_size=0.2, random_state=42
)

# Classification model: Logistic Regression
clf_pipeline = Pipeline(steps=[
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

# Regression model: Linear Regression
reg_pipeline = Pipeline(steps=[
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])

# Train models
clf_pipeline.fit(X_train, y_class_train)
reg_pipeline.fit(X_train, y_reg_train)

# ---------- 2. ROUTES ----------

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    prediction = None
    probability = None
    predicted_score = None

    if request.method == "POST":
        try:
            hours_studied = float(request.form["hours_studied"])
            attendance = float(request.form["attendance"])
            previous_score = float(request.form["previous_score"])
            assignments_completed = int(request.form["assignments_completed"])

            # Create input DataFrame
            input_df = pd.DataFrame([{
                "hours_studied": hours_studied,
                "attendance": attendance,
                "previous_score": previous_score,
                "assignments_completed": assignments_completed
            }])

            # Classification: Pass/Fail
            class_pred = clf_pipeline.predict(input_df)[0]
            class_proba = clf_pipeline.predict_proba(input_df)[0][1]  # prob of pass (1)

            # Regression: Predicted final score
            score_pred = reg_pipeline.predict(input_df)[0]

            prediction = int(class_pred)
            probability = round(float(class_proba) * 100, 1) # Convert to percentage
            predicted_score = round(float(score_pred), 1)

            # Cap the score at 100
            if predicted_score > 100:
                predicted_score = 100.0

        except Exception as e:
            print("Error:", e)

    return render_template(
        "predict.html",
        prediction=prediction,
        probability=probability,
        predicted_score=predicted_score
    )

if __name__ == "__main__":
    app.run(debug=True)