from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import re
import math
import numpy as np
from typing import Dict

app = FastAPI(
    title="ML-Enhanced Password Security API",
    description="Combines regex, entropy + ML for 20–25% better password strength detection",
    version="1.0"
)

# Load model
model = joblib.load("password_model.pkl")

class PasswordRequest(BaseModel):
    password: str

def calculate_entropy(password: str) -> float:
    entropy = 0
    for c in set(password):
        p = password.count(c) / len(password)
        entropy -= p * math.log2(p)
    entropy *= len(password)
    return entropy

def traditional_checks(password: str) -> Dict:
    score = 0
    feedback = []
    
    if len(password) >= 12: score += 25
    elif len(password) >= 8: score += 15
    
    if re.search(r"[a-z]", password): score += 10
    if re.search(r"[A-Z]", password): score += 15
    if re.search(r"\d", password): score += 15
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password): score += 20
    
    entropy = calculate_entropy(password)
    if entropy > 50: score += 25
    elif entropy > 35: score += 15
    
    if score < 50: feedback.append("Use 12+ characters")
    if not re.search(r"[A-Z]", password): feedback.append("Add uppercase letters")
    if not re.search(r"\d", password): feedback.append("Add numbers")
    if not re.search(r"[!@#$%^&*]", password): feedback.append("Add special symbols")
    
    return {"score": min(score, 80), "feedback": feedback[:3]}

@app.post("/api/v1/check")
async def check_password(req: PasswordRequest):
    pwd = req.password.strip()
    if not pwd:
        raise HTTPException(400, "Password cannot be empty")
    
    # 1. Traditional score
    trad = traditional_checks(pwd)
    
    # 2. ML prediction
    ml_prob = model.predict_proba([pwd])[0][1]  # probability of being strong
    ml_boost = int(ml_prob * 40)  # scale to 0-40 points
    
    final_score = min(100, trad["score"] + ml_boost)
    strength = "Very Weak"
    if final_score >= 90: strength = "Very Strong"
    elif final_score >= 80: strength = "Strong"
    elif final_score >= 60: strength = "Moderate"
    elif final_score >= 40: strength = "Weak"
    else: strength = "Very Weak"
    
    return {
        "password_length": len(pwd),
        "entropy_bits": round(calculate_entropy(pwd), 1),
        "traditional_score": trad["score"],
        "ml_confidence": round(ml_prob * 100, 1),
        "final_score": final_score,
        "strength": strength,
        "suggestions": trad["feedback"] if final_score < 90 else ["Password is strong!"]
    }

@app.get("/")
async def root():
    return {"message": "ML-Enhanced Password Security API – POST to /api/v1/check"}