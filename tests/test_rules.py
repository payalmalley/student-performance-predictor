import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rules import evaluate_student

def test_strong_student():
    result = evaluate_student(attendance=95, marks=90, study_hours=6)
    assert result["category"] == "Good Progress"

def test_multiple_warning_indicators():
    result = evaluate_student(attendance=40, marks=35, study_hours=1)
    assert result["category"] == "At Risk"

def test_mixed_indicators_high_attendance_low_marks():
    result = evaluate_student(attendance=90, marks=40, study_hours=3)
    assert result["category"] in ("Average Progress", "At Risk")

def test_low_attendance_high_marks_not_same_as_both_low():
    low_both = evaluate_student(attendance=30, marks=30, study_hours=1)
    low_attendance_only = evaluate_student(attendance=30, marks=90, study_hours=5)
    assert low_attendance_only["score"] > low_both["score"]

def test_invalid_input():
    result = evaluate_student(attendance=-20, marks=150, study_hours=-5)
    assert result["valid"] is False
    assert len(result["errors"]) > 0