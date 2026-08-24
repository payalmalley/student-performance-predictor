def evaluate_student(attendance, marks, study_hours):
    """
    Takes raw student indicators, returns a progress category and reasons.
    Uses a simple point-based scoring system (see spec section 11).
    """
    # --- Input validation ---
    errors = []
    if not (0 <= attendance <= 100):
        errors.append("Attendance must be between 0 and 100.")
    if not (0 <= marks <= 100):
        errors.append("Marks must be between 0 and 100.")
    if study_hours < 0:
        errors.append("Study hours cannot be negative.")
    if errors:
        return {"valid": False, "category": "Error", "reasons": errors}

    # --- Scoring ---
    # Attendance: up to 40 points
    attendance_score = (attendance / 100) * 40
    # Marks: up to 40 points
    marks_score = (marks / 100) * 40
    # Study hours: up to 20 points (capped at 10 hrs/day = full points)
    study_score = min(study_hours / 10, 1) * 20

    total_score = attendance_score + marks_score + study_score

    # --- Category ---
    if total_score >= 80:
        category = "Good Progress"
    elif total_score >= 50:
        category = "Average Progress"
    else:
        category = "At Risk"

    # --- Reasons (explanation) ---
    reasons = []
    if attendance < 60:
        reasons.append("Attendance is below the healthy range.")
    elif attendance >= 85:
        reasons.append("Attendance is strong.")

    if marks < 50:
        reasons.append("Recent marks are below the healthy range.")
    elif marks >= 75:
        reasons.append("Marks are strong.")

    if study_hours < 2:
        reasons.append("Study hours are low.")
    elif study_hours >= 5:
        reasons.append("Study habits look solid.")

    if not reasons:
        reasons.append("Indicators are moderate across the board.")

    return {
        "valid": True,
        "score": round(total_score, 1),
        "category": category,
        "reasons": reasons,
    }