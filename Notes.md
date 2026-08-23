# NOTES

**Phase:** 1 — Rule-based prototype (no ML)

## Contract
- Route: `POST /predict`
- Fields: `role`, `attendance`, `marks`, `marks_history`, `grade`
- Template vars: `result.category`, `result.reasons`
- `marks_history`: comma-separated string, e.g. `"72,68,75,80"`

## Color palette
- Burgundy: `#6B2D3C`
- Warm Grey: `#E8E3DC`
- Dark text: `#2A2222`

## Done
- `README.md` — Payal
- `.gitignore` — Mohit
- `NOTES.md` — Mohit
- `index.html` — Mohit
 
- ## Backend — Progress Note

**Date:** 2026-08-23
**Contributor: Payal (backend)

### What was done
- Set up project folder structure for Phase 1 (rule-based prototype, no ML/DB/auth yet)
- Fixed local environment issue: Python wasn't actually installed (only a Windows Store alias was present); installed Python 3.13 properly and disabled the conflicting Store alias
- Created virtual environment (`venv`) and installed dependencies (`Flask`, `pytest`)
- Wrote `rules.py` — core scoring logic:
  - Point-based system: Attendance (up to 40 pts), Marks (up to 40 pts), Study hours (up to 20 pts, capped at 10 hrs/day)
  - Categories: Good Progress (≥80), Average Progress (50–79), At Risk (<50)
  - Includes input validation (rejects out-of-range attendance/marks, negative study hours)
  - Returns a plain-language list of reasons behind the result
- Wrote `app.py` — Flask route (`/`) that accepts GET/POST, reads form input, calls `rules.py`, renders `index.html` with the result
- Wrote `tests/test_rules.py` — 5 unit tests covering: strong student, multiple warning indicators, mixed indicators, low-attendance-vs-both-low comparison, invalid input handling
- Ran `pytest tests/` — **all 5 tests passed**
- Verified Flask server boots correctly (`python app.py` → running on `http://127.0.0.1:5000`)

### Contract shared with frontend
- Form field names: `attendance`, `marks`, `study_hours`
- Template variables available in `index.html`: `result.valid`, `result.errors`, `result.score`, `result.category`, `result.reasons`

### Status
Backend logic for Phase 1 is functionally complete and tested. Waiting on frontend (`templates/index.html`, `static/style.css`) to be built against the contract above before end-to-end testing in the browser.

### Next steps (backend side)
- Once frontend is ready, do an end-to-end test in the browser with real form submissions
- Write `requirements.txt` pin versions (currently just `Flask`)
- Add `.gitignore` (venv/, __pycache__/, etc.) before pushing to GitHub
