import joblib, numpy as np
from typing import List
model = joblib.load("app/model_rf.joblib")
binarizer = joblib.load("app/symptom_binarizer.joblib")

def predict_conditions(symptoms: List[str], top_k: int = 3):
    xs = [s.strip().lower() for s in symptoms]
    X = binarizer.transform([xs])
    proba = None
    if hasattr(model, "predict_proba"):
        # map proba to class labels
        proba = model.predict_proba(X)[0]
        classes = model.classes_
        pairs = sorted(zip(classes, proba), key=lambda p: p[1], reverse=True)[:top_k]
        return [{"condition": c, "probability": float(p)} for c,p in pairs]
    pred = model.predict(X)[0]
    return [{"condition": pred, "probability": 0.0}]
