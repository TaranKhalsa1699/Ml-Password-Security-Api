import math

def calculate_entropy(password):
    pool = 0
    if any(c.islower() for c in password): pool += 26
    if any(c.isupper() for c in password): pool += 26
    if any(c.isdigit() for c in password): pool += 10
    if any(c in "!@#$%^&*()-_=+[]{};:,.<>?/|\\`~" for c in password): pool += 30

    if pool == 0:
        return 0
    return len(password) * math.log2(pool)

def rule_score(password):
    score = 0
    if len(password) >= 8: score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c in "!@#$%^&*" for c in password): score += 1
    return score

def create_features(df):
    df["length"] = df["password"].apply(len)
    df["entropy"] = df["password"].apply(calculate_entropy)
    df["rule_score"] = df["password"].apply(rule_score)
    return df
