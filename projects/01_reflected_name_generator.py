
# Reflected Name Generator
# This program takes a name as input and generates a reflected version using simple formatting.

# Step 1: Ask the user to enter their name
name = input("Enter your name: ")

# Step 2: Create a reflected version of the name
# The reflected version combines the original name with its reverse
reflected_name = name[::-1]
print(reflected_name)

# Step 3: Print each character of the reflected name surrounded by asterisks
# for char in reflected_name:
#     print(f"* {char} *")
