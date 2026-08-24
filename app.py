from flask import Flask, render_template, request
from rules import evaluate_student

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            attendance = float(request.form.get("attendance", ""))
            marks = float(request.form.get("marks", ""))
            study_hours = float(request.form.get("study_hours", ""))
            result = evaluate_student(attendance, marks, study_hours)
        except ValueError:
            result = {
                "valid": False,
                "category": "Error",
                "reasons": ["Please enter valid numbers in all fields."],
            }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)