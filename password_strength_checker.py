import re

def check_password_strength(password):
    strength_score = 0
    feedback = []

    if len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if re.search(r'\d', password):
        strength_score += 1
    else:
        feedback.append("Include at least one digit.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_score += 1
    else:
        feedback.append("Include at least one special character.")

    # Final rating
    if strength_score == 5:
        rating = "Very Strong"
    elif strength_score >= 3:
        rating = "Moderate"
    else:
        rating = "Weak"

    return rating, feedback



print("🔐 Password Strength Checker")
password = input("Enter your password: ")

rating, feedback = check_password_strength(password)

print(f"\nPassword Rating: {rating}")
if feedback:
    print("Suggestions to improve your password:")
    for tip in feedback:
        print(f"- {tip}")
