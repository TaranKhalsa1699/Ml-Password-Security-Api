from pydantic import BaseModel

class PasswordRequest(BaseModel):
    password: str

class PasswordResponse(BaseModel):
    entropy: float
    rule_score: int
    ml_prediction: int
    final_strength: str
    breach_count: int
    suggestions: list
