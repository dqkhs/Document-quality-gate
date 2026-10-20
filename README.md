# Document Quality Gate — QA Automation Project

An automated quality gate built with Python, pytest, and Hypothesis to validate LLM-generated Markdown documentation against structural and content standards before publishing.

## Problem Statement

AI/LLM-generated documentations often suffer from:

- Missing critical sections (e.g., Acceptance Criteria).
- Duplicate or non-standard Requirement IDs (`REQ-XXX`).
- Ambiguous notes left behind (`TODO`, `TBD`, `UNCLEAR`).

This project serves as an automated quality gate to catch these flaws deterministically before deployment or documentation sync.

## Features

- **Structural Validation:** Ensures required sections exist (`## Overview`, `## Requirements`, `## Acceptance Criteria`).
- **Requirement ID Tracking:** Detects duplicate or missing `REQ-XXX` tags using regular expressions.
- **Unclear Note Detection:** Scans for placeholder tags like `TODO`, `TBD`, or `UNCLEAR`.
- **Property-Based Testing:** Uses `Hypothesis` to generate fuzzing inputs and test edge cases automatically.
- **CLI Gate Execution:** Returns exit codes (`0` for PASS, `1` for FAIL) suitable for CI/CD pipelines.

## Tech Stack

- **Language:** Python 3.12+
- **Testing Frameworks:** `pytest`, `Hypothesis`
- **Version Control:** Git, GitHub

## Project Structure

```
document-quality-gate/
├── validator.py
├── cli.py
├── test_validator.py
├── test_hypothesis.py
├── samples/
│   ├── valid.md
│   └── invalid.md
└── readme.md
```

## Quick Start

### 1. Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/dqkhs/Document-quality-gate.git
cd Document-quality-gate
pip install -r requirements.txt
```

### 2. Usage (CLI)

Run the Quality Gate against any Markdown document:

```bash
# Valid document (returns Exit Code 0)
python cli.py samples/valid.md

# Invalid document (returns Exit Code 1)
python cli.py samples/invalid.md
```

### 3. Running Tests

Run unit tests and property-based tests using `pytest`:

```bash
python -m pytest -v
```
