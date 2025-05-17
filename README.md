# cgpa-calc 🧮

A command-line tool to analyze academic transcripts from a TOML file. It computes SGPA, CGPA, and rolling CGPA with a clean `rich`-powered interface.

> Tailored for the grading system used at Shiv Nadar Institution of Eminence

## Features
- **Semester View**: Course details, credits, grades, SGPA.
- **CGPA Summary**: Cumulative stats and per-semester breakdown.
- **Interactive CLI**: Simple, menu-based navigation.
- **TOML Input**: All data comes from a single `grades.toml` file.

## Requirements

- Python 3.11+ (uses `tomllib`)
- `uv` (or any Python virtual environment manager)
- `rich`

## Setup
1. Clone this repository

```bash
git clone https://github.com/lalitm1004/cgpa-calc.git
cd cgpa-calc
```

2. Install requirements
```bash
uv sync
```

3. Create `grades.toml` based on the provided `grades.example.toml`

4. Run using
```bash
uv run src/main.py
```
## Grade Mapping

| Grade | Points |
|-------|--------|
| A     | 10.0   |
| A-    | 9.0    |
| B     | 8.0    |
| B-    | 7.0    |
| C     | 6.0    |
| C-    | 5.0    |
| D     | 4.0    |
| E     | 2.0    |
| F/F*  | 0.0    |

Grades outside this list are ignored in GPA calculations.

## [Composition](https://github.com/lalitm1004/composition)
```bash
$ composition
Python | 260 lines | 100.00% | ██████████████████████████████████████████████████
```