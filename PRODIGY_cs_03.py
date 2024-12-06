import re
import getpass

print("---------------- Password Complexity Checking Tool -----------------")

def assess_password_strength(password: str) -> str:
    """
    Evaluates the strength of a password based on several criteria:
    - Contains numbers
    - Contains both uppercase and lowercase letters
    - Meets minimum length requirement
    - Contains special characters
    """
    has_numbers = any(char.isdigit() for char in password)
    
    has_upper_lower_case = any(char.isupper() for char in password) and any(char.islower() for char in password)
    
    meets_length_requirement = len(password) >= 8
    
    has_special_characters = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    
    met_criteria_count = sum([has_numbers, has_upper_lower_case, meets_length_requirement, has_special_characters])
    
    if met_criteria_count == 4:
        return "Password Strength Level: Very Strong (All criteria are met)."
    elif met_criteria_count == 3:
        return "Password Strength Level: Moderately Strong (Three criteria are met)."
    elif met_criteria_count == 2:
        return "Password Strength Level: Strong (Two criteria are met)."
    else:
        return "Password Strength Level: Weak (Fewer than two criteria are met)."

password_input = getpass.getpass("Enter your password: ")

masked_password = password_input[0] + '#' * (len(password_input) - 2) + password_input[-1]

result = assess_password_strength(password_input)

print(f"\nEntered Password: {masked_password}")
print(f"\n{result}\n")

tips = [
    "Here are some quick tips for creating a secure password:",
    "1. Length: Aim for at least 12 characters.",
    "2. Mix Characters: Use a combination of uppercase, lowercase, numbers, and symbols.",
    "3. Avoid Common Words: Don't use easily guessable information.",
    "4. No Personal Info: Avoid using names, birthdays, or personal details.",
    "5. Use Passphrases: Consider combining multiple words or a sentence.",
    "6. Unique for Each Account: Don't reuse passwords across multiple accounts.",
    "7. Regular Updates: Change passwords periodically.",
    "8. Enable 2FA: Use Two-Factor Authentication where possible.",
    "9. Be Wary of Phishing: Avoid entering passwords on suspicious sites.",
    "10. Password Manager: Consider using one for secure and unique passwords."
]

for tip in tips:
    print(tip)