import random

# Character set for generating passwords (includes uppercase, lowercase, numbers, and special symbols)
char_set = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?<>{}'

# Prompt the user for the desired password length
password_length = int(input('Enter the desired length of your password (recommended: 14 or more characters): '))

# Generate a random password using sampling without replacement
generated_password = ''.join(random.sample(char_set, password_length))

# Print the generated password
print('Your strong password is:', generated_password)