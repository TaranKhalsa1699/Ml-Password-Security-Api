import re

def evaluate_rules(password):
    score = 0
    suggestions = []

    if len(password) >= 8: score += 20
    else: suggestions.append("Use at least 8 characters")

    if re.search(r"[A-Z]", password): score += 20
    else: suggestions.append("Add uppercase letters")

    if re.search(r"[a-z]", password): score += 20
    else: suggestions.append("Add lowercase letters")

    if re.search(r"[0-9]", password): score += 20
    else: suggestions.append("Add numbers")

    if re.search(r"[!@#$%^&*()_+]", password): score += 20
    else: suggestions.append("Add symbols")

    return score, suggestions
