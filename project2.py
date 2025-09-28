# Digital Phone Book 📞
import json
import os

# File to store users and contacts
DATA_FILE = "phonebook.json"

# Load existing data or initialize empty
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as f:
        phonebook_data = json.load(f)
else:
    phonebook_data = {}

# Save data function
def save_data():
    with open(DATA_FILE, 'w') as f:
        json.dump(phonebook_data, f, indent=4)

# Registration
def register():
    username = input("Enter username: ")
    if username in phonebook_data:
        print("Username already exists! Try login.")
        return None
    password = input("Enter password: ")
    phonebook_data[username] = {"password": password, "contacts": {}}
    save_data()
    print(f"User {username} registered successfully!")
    return username

# Login
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in phonebook_data and phonebook_data[username]["password"] == password:
        print(f"Welcome back, {username}!")
        return username
    else:
        print("Invalid credentials!")
        return None

# Add contact
def add_contact(user):
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    phonebook_data[user]["contacts"][name] = number
    save_data()
    print(f"Contact '{name}' added successfully!")

# Read all contacts
def read_all_contacts(user):
    contacts = phonebook_data[user]["contacts"]
    if contacts:
        print("All contacts:")
        for name, number in contacts.items():
            print(f"{name}: {number}")
    else:
        print("No contacts found!")

# Read specific contact
def read_contact(user):
    name = input("Enter contact name to search: ")
    contacts = phonebook_data[user]["contacts"]
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"Contact '{name}' not found.")

# Update contact
def update_contact(user):
    name = input("Enter contact name to update: ")
    contacts = phonebook_data[user]["contacts"]
    if name in contacts:
        new_number = input(f"Enter new number for {name}: ")
        contacts[name] = new_number
        save_data()
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"Contact '{name}' not found.")

# Delete contact
def delete_contact(user):
    name = input("Enter contact name to delete: ")
    contacts = phonebook_data[user]["contacts"]
    if name in contacts:
        del contacts[name]
        save_data()
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found.")

# Delete all contacts
def delete_all_contacts(user):
    phonebook_data[user]["contacts"].clear()
    save_data()
    print("All contacts deleted successfully!")

# Main menu
def phonebook_menu(user):
    while True:
        print("\n--- Phone Book Menu ---")
        print("1. Add Contact")
        print("2. Read All Contacts")
        print("3. Read Specific Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Delete All Contacts")
        print("7. Logout")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_contact(user)
        elif choice == '2':
            read_all_contacts(user)
        elif choice == '3':
            read_contact(user)
        elif choice == '4':
            update_contact(user)
        elif choice == '5':
            delete_contact(user)
        elif choice == '6':
            delete_all_contacts(user)
        elif choice == '7':
            print(f"Goodbye, {user}!")
            break
        else:
            print("Invalid choice! Try again.")

# Authentication menu
def main():
    print("Welcome to Digital Phone Book 📞")
    while True:
        print("\n--- Main Menu ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            user = register()
            if user:
                phonebook_menu(user)
        elif choice == '2':
            user = login()
            if user:
                phonebook_menu(user)
        elif choice == '3':
            print("Exiting Phone Book. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
