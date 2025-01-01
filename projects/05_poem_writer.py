
# Poem Writer
# Write and save your own poems to a file.

# Step 1: Ask the user to write their poem
filename = "poems.txt"

print("Welcome to the Poem Writer!")
poem = input("Write your poem (end with an empty line):\n")

# Step 2: Save the poem to a file
with open(filename, "w") as file:
    file.write(poem)

# Step 3: Notify the user of success
print(f"Your poem has been saved to {filename}.")
