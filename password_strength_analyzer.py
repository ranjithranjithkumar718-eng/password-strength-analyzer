import argparse
import re
import string


def analyze_password(password: str):
    if not password:
        return {
            "score": 0,
            "label": "Weak",
            "feedback": ["Password is empty."],
            "checks": {},
        }

    checks = {
        "length_ok": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digits": bool(re.search(r"\d", password)),
        "special": bool(re.search(r"[^A-Za-z0-9]", password)),
    }

    score = 0
    feedback = []

    if len(password) >= 8:
        score += 20
    else:
        score += len(password) * 2
        feedback.append("Use at least 8 characters.")

    if checks["uppercase"]:
        score += 20
    else:
        feedback.append("Add uppercase letters.")

    if checks["lowercase"]:
        score += 20
    else:
        feedback.append("Add lowercase letters.")

    if checks["digits"]:
        score += 20
    else:
        feedback.append("Add numbers.")

    if checks["special"]:
        score += 20
    else:
        feedback.append("Add special characters.")

    if len(password) >= 12:
        score += 10
    if not re.search(r"(.)\1{2,}", password):
        score += 10
    if not re.search(r"(123|password|qwerty|admin|welcome)", password.lower()):
        score += 10

    score = max(0, min(100, score))

    if score < 40:
        label = "Weak"
    elif score < 60:
        label = "Fair"
    elif score < 80:
        label = "Good"
    elif score < 90:
        label = "Strong"
    else:
        label = "Very Strong"

    if re.search(r"(.)\1{2,}", password):
        feedback.append("Avoid repeated characters and sequences.")
    if re.search(r"(123|password|qwerty|admin|welcome)", password.lower()):
        feedback.append("Avoid common words and predictable patterns.")

    if not feedback:
        feedback.append("Excellent password strength.")

    return {
        "score": score,
        "label": label,
        "feedback": feedback,
        "checks": checks,
    }


def print_result(result):
    print(f"Password strength: {result['label']}")
    print(f"Score: {result['score']}/100")
    print("Checks:")
    for key, value in result["checks"].items():
        status = "Yes" if value else "No"
        print(f"  - {key}: {status}")
    print("Suggestions:")
    for item in result["feedback"]:
        print(f"  - {item}")


def main():
    parser = argparse.ArgumentParser(description="Analyze the strength of a password.")
    parser.add_argument("--password", help="Password to evaluate.")
    args = parser.parse_args()

    if args.password is not None:
        result = analyze_password(args.password)
        print_result(result)
        return

    user_input = input("Enter a password to evaluate: ")
    result = analyze_password(user_input)
    print_result(result)


if __name__ == "__main__":
    main()
