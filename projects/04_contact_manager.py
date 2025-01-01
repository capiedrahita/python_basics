
# Contact Manager
# A simple contact manager that allows adding, searching, and removing contacts.

# Step 1: Initialize an empty dictionary to store contacts
contacts = {}

# Step 2: Define functions for adding, searching, and removing contacts
def add_contact(name, phone):
    contacts[name] = phone
    print(f"Added: {name} -> {phone}")

def search_contact(name):
    if name in contacts:
        print(f"Found: {name} -> {contacts[name]}")
    else:
        print(f"{name} not found in contacts.")

def remove_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Removed: {name}")
    else:
        print(f"{name} not found in contacts.")

# Step 3: Provide a menu for the user to interact with the contact manager
while True:
    print("Options: [1] Add [2] Search [3] Remove [4] Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_contact(name, phone)
    elif choice == "2":
        name = input("Enter name to search: ")
        search_contact(name)
    elif choice == "3":
        name = input("Enter name to remove: ")
        remove_contact(name)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
