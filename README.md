# Student Performance Predictor

A lightweight, browser-based application that estimates a student's academic performance using predefined rules based on academic and behavioral indicators.

> **Current Status: Phase 1 — Rule-Based Prototype**
> This project does **not** currently use Machine Learning. It uses manually defined rules/scoring, and should not be described as an ML system until a trained model actually exists.

---

## Table of Contents

- [About](#about)
- [Project Goals](#project-goals)
- [Current Phase: Rule-Based Prototype](#current-phase-rule-based-prototype)
- [How the System Works](#how-the-system-works)
- [Input Features](#input-features)
- [Prediction Categories](#prediction-categories)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Testing](#testing)
- [Limitations](#limitations)
- [Privacy & Ethics](#privacy--ethics)
- [Roadmap](#roadmap)
- [Collaboration](#collaboration)
- [Disclaimer](#disclaimer)
- [License](#license)
- [Contributors](#contributors)

---

## About

**Student Performance Predictor** is a collaborative project exploring how basic student-related indicators can be used to estimate academic performance.

The project is being built in deliberate stages. The first stage is a simple **rule-based prototype** built with Python and Flask. Rather than reaching for Machine Learning right away, the system evaluates student inputs against predefined conditions (or a simple scoring system) to generate a basic performance category.

Once this prototype is working and the underlying concept has been validated, the project may be extended into a Machine Learning-based prediction system, using an appropriately selected and analyzed dataset.

## Project Goals

- Build a simple, understandable student performance prediction system.
- Create a functional, browser-based prototype.
- Experiment with different academic and behavioral indicators.
- Validate the basic concept before introducing Machine Learning.
- Eventually investigate whether an ML model can improve on the rule-based approach.
- Learn practical development and collaboration using Git and GitHub.

The goal is **not** to build the largest or most complicated version of this project — it's to build something that actually works, and can progressively grow stronger from there.

## Current Phase: Rule-Based Prototype

Phase 1 focuses exclusively on a working initial prototype. The system will:

1. Collect basic student information through a web interface.
2. Pass that information to the Python/Flask backend.
3. Validate the inputs.
4. Evaluate the inputs using predefined rules or a scoring system.
5. Generate a performance category.
6. Display the result — along with a brief explanation of why that category was produced.

```text
Student Input
     │
     ▼
Input Validation
     │
     ▼
Python / Flask
     │
     ▼
Rule-Based Evaluation
     │
     ▼
Performance Category + Explanation
     │
     ▼
Result Display
```

## How the System Works

The Phase 1 system uses **predefined conditions**, not a trained Machine Learning model.

Example rule:

```text
IF attendance >= 80%
AND marks >= 70%
AND assignment performance is good
        ↓
   Good Performance
```

Other input combinations may result in **Average Performance** or **At Risk**. Rules will be refined during development and testing, and may eventually be replaced or supplemented by a simple points-based scoring system if the rule set grows too complex.

The system aims to explain its output rather than just state it, e.g.:

```text
Prediction: At Risk

Reasons:
- Attendance is below the selected threshold.
- Recent marks are below the selected range.
- Assignment completion is low.

Suggested focus:
Improve attendance and assignment consistency.
```

The system describes *patterns in indicators*, not guaranteed outcomes — it does not claim to know a student's future, and does not claim causation between any single indicator and academic outcomes.

## Input Features

Potential indicators under consideration:

**Academic**
- Attendance percentage
- Test/examination marks
- Previous academic performance
- Assignment performance

**Behavioral**
- Study hours
- Missed assignments
- Missed classes

The final set of features used will be determined during development — a feature is only included if there's a reasonable justification for why it contributes to estimating performance.

## Prediction Categories

| Category | Description |
|---|---|
| 🟢 Good Performance | Current indicators suggest the student is progressing well. |
| 🟡 Average Performance | Indicators are mixed or moderate; some areas may need improvement. |
| 🔴 At Risk | Multiple indicators suggest the student may need additional academic attention. |

These categories and their definitions are simplified and may change as the prototype is developed and tested.

## Technology Stack

**Current (Phase 1)**
- Python
- Flask
- HTML
- CSS
- Git / GitHub

**Planned for a future ML phase (not yet in use)**
- NumPy
- Pandas
- Scikit-learn
- Matplotlib

Future dependencies will not be installed until they're actually needed.

## Project Structure

```text
student-performance-predictor/
│
├── app.py
├── rules.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── tests/
│   └── test_rules.py
│
├── README.md
├── .gitignore
└── LICENSE
```

This structure may evolve as development progresses.

## Getting Started

### Prerequisites

- Python 3.x
- pip
- Git

### Clone the repository

```bash
git clone https://github.com/payalmalley/student-performance-predictor.git
cd student-performance-predictor
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Then open the local URL Flask provides in your browser.

> Exact setup and run commands may change as the project develops.

## Testing

Phase 1 testing focuses on whether the rule-based system produces reasonable, consistent results across different input combinations, including:

- High-performing students
- Average-performing students
- Students with low attendance but strong marks
- Students with good attendance but weak marks
- Multiple simultaneous warning indicators
- Edge cases and invalid/missing input (e.g. out-of-range attendance, non-numeric marks, negative study hours)

The goal is to catch inconsistent or unrealistic predictions before moving toward later phases.

## Limitations

- Based on manually defined rules, not learned from historical data.
- Predictions are not scientifically validated.
- Cannot establish causal relationships between student behavior and academic outcomes.
- Prediction categories are simplified.
- Results may not generalize to real-world student populations.

These limitations are expected to be addressed, where possible, in later phases.

## Privacy & Ethics

Student-related information can be sensitive. If real student data is used in future phases:

- Data should be collected or obtained legally.
- Personally identifiable information should be avoided wherever possible.
- Data should be anonymized where appropriate.
- Appropriate consent and institutional requirements should be considered.
- The system should not be used to make high-stakes decisions about students without appropriate validation and human oversight.

## Roadmap

### Phase 1 — Rule-Based Prototype
- [ ] Design the initial UI
- [ ] Define input fields
- [ ] Implement the Flask backend
- [ ] Create the rule-based/scoring prediction logic
- [ ] Display prediction results with reasoning
- [ ] Test different input combinations
- [ ] Document the prototype

### Phase 2 — Data & Validation
- [ ] Define a clear ML target (e.g. pass/fail, risk of academic failure, semester performance)
- [ ] Identify an appropriate dataset
- [ ] Collect or obtain data legally and ethically
- [ ] Analyze and clean the dataset
- [ ] Identify relevant features
- [ ] Compare the dataset against the existing rules

### Phase 3 — Machine Learning
- [ ] Prepare training/testing data
- [ ] Establish baseline models (e.g. Logistic Regression, Decision Tree, Random Forest)
- [ ] Train and evaluate candidate models
- [ ] Compare appropriate metrics (accuracy, precision, recall, F1, ROC-AUC as relevant)
- [ ] Select a suitable model

### Phase 4 — Deployment
- [ ] Integrate the trained model with the web application
- [ ] Prepare the production environment
- [ ] Deploy and test with unseen data
- [ ] Improve reliability and usability

The project will not move to Machine Learning until the Phase 1 concept and prototype have been implemented and evaluated.

## Collaboration

This project is being developed collaboratively, with responsibilities divided according to technical needs and available hardware resources. Resource-intensive tasks (large-scale data processing, model training) will be moved to a more capable machine or cloud resources when that becomes necessary, rather than during Phase 1.

Both contributors participate in development, testing, technical decisions, documentation, and the Git/GitHub workflow. Development follows a simple branch-based workflow (`feature/*` branches merged into `main` via pull request) rather than large, unreviewed commits.

## Disclaimer

This project is intended for educational and experimental purposes. The Phase 1 output represents a rule-based estimate and should not be treated as an authoritative assessment of a student's academic ability, future performance, or educational outcome.

A future Machine Learning version will only be presented as a prediction system after being properly trained, tested, and evaluated on appropriate data.

## License

License: To be decided

## Contributors

- [Contributor 1 — GitHub Profile]
- [Contributor 2 — GitHub Profile]
