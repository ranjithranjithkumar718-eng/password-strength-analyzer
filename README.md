# Password Strength Analyzer

A lightweight Python project that checks whether a password is weak, moderate, strong, or very strong.

## Features

- Checks length
- Verifies uppercase, lowercase, digits, and symbols
- Detects repeated characters and common password patterns
- Gives a score from 0 to 100
- Prints actionable suggestions

## Setup

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python password_strength_analyzer.py --password "TestPass123!"
```

Or run interactively:

```bash
python password_strength_analyzer.py
```

## Build

```bash
python -m pip install .
```
