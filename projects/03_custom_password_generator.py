
# Custom Password Generator
# Generate passwords based on user preferences.

import random
import string

# Step 1: Greet the user and ask for their password preferences
print("Welcome to the Custom Password Generator!")

length = int(input("Enter the desired password length: "))
include_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
include_specials = input("Include special characters? (yes/no): ").lower() == "yes"

# Step 2: Build the character pool based on user preferences
characters = string.ascii_letters
if include_numbers:
    characters += string.digits
if include_specials:
    characters += string.punctuation

# Step 3: Generate a random password from the character pool
password = "".join(random.choice(characters) for _ in range(length))
print(f"Your generated password is: {password}")
