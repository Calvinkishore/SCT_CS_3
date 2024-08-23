import re

def calculate_password_strength(password):
    # Initialize strength variables
    length_score = 0
    uppercase_score = 0
    lowercase_score = 0
    number_score = 0
    special_char_score = 0

    # Evaluate password length
    if len(password) >= 8:
        length_score = 2
    elif len(password) >= 6:
        length_score = 1

    # Evaluate presence of uppercase letters
    if re.search(r'[A-Z]', password):
        uppercase_score = 1

    # Evaluate presence of lowercase letters
    if re.search(r'[a-z]', password):
        lowercase_score = 1

    # Evaluate presence of numbers
    if re.search(r'[0-9]', password):
        number_score = 1

    # Evaluate presence of special characters
    if re.search(r'[@$!%*?&#^]', password):
        special_char_score = 2

    # Calculate total score
    total_score = length_score + uppercase_score + lowercase_score + number_score + special_char_score

    # Determine password strength based on total score
    if total_score >= 7:
        strength = "Very Strong"
    elif total_score >= 5:
        strength = "Strong"
    elif total_score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, total_score

password = input("Enter a password: ")
strength, score = calculate_password_strength(password)
print(f"Password Strength: {strength} (Score: {score}/7)")
