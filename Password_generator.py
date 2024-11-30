import random
import string

# Function to generate a random password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Accept user input for the password length
password_length = int(input("Enter the desired password length: "))
password = generate_password(password_length)

# Display the result
print(f"Generated Password: {password}")

