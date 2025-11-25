from fastapi import APIRouter
from api.schemas import PasswordRequest, PasswordResponse
from core.password_rules import evaluate_rules
from core.entropy import calculate_entropy
from core.breach_checker import check_breach
import pickle
import numpy as np

router = APIRouter()

# Load ML Model
model = pickle.load(open("ml/model.pkl", "rb"))

@router.post("/check_password", response_model=PasswordResponse)
def check_password(req: PasswordRequest):

    entropy_val = calculate_entropy(req.password)
    rule_score, suggestions = evaluate_rules(req.password)

    # ML Prediction
    X = np.array([[len(req.password), entropy_val, rule_score]])
    ml_pred = model.predict(X)[0]

    # Breach Check
    breach_count = check_breach(req.password)

    final_strength = "Weak"
    if rule_score > 60 and ml_pred == 2:
        final_strength = "Strong"
    elif rule_score > 40:
        final_strength = "Medium"

    return PasswordResponse(
        entropy=entropy_val,
        rule_score=rule_score,
        ml_prediction=int(ml_pred),
        final_strength=final_strength,
        breach_count=breach_count,
        suggestions=suggestions
    )
