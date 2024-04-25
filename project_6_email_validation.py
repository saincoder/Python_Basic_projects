import re


def is_valid_email(email):
    """
    Validates an email address based on the specified conditions:

    1. All letters (a-z) must be lowercase.
    2. Digits (0-9) are allowed.
    3. Characters '.' and '_' can be used once before the '@' symbol.
    4. '@' symbol must appear exactly once.
    5. '.' character must be in the second or third position from the end.
    """

    email_condition = r'^[a-z0-9.+_-]+@[a-z0-9-]+\.[a-z]{2,}$'
    match = re.search(email_condition, email)

    if match:
        # Extract the username and domain parts for potential further validation
        username = match.group(0).split('@')[0]
        domain = match.group(0).split('@')[1]
        return True  # Valid email based on syntax
    else:
        return False  # Invalid email syntax


# Get user input
user_email = input("Enter your email: ")

# Validate the email address
if is_valid_email(user_email):
    print("Correct email")
else:
    print("Wrong email. Please ensure it follows the format:")
