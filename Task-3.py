import json
import os

Contacts_File = "contacts.json"

def load_contacts():
    if os.path.exists(Contacts_File):
        with open(Contacts_File,"r") as file:
            return json.load(file)
    return[]

def save_contacts(contacts):
    with open(Contacts_File,"w") as file:
        json.dump(contacts,file, indent=4)

def add_contacts(contacts):
    name = input("Enter Name: ")
    Phone = input("Enter the phone number: ")
    email = input("Enter email address: ")
    contacts.append({"name": name, "Phone": Phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contatcs found")
        return
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name:{contact['name']}, Phone: {contact['Phone']}, Email: {contact['email']}")

def edit_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        index = int(input("Enter the number of the contact to edit: ")) - 1
        if 0 <= index < len(contacts):
            contacts[index]["name"] = input(f"Enter new name (current: {contacts[index]['name']}): ") or contacts[index]["name"]
            contacts[index]["phone"] = input(f"Enter new phone (current: {contacts[index]['Phone']}): ") or contacts[index]["phone"]
            contacts[index]["email"] = input(f"Enter new email (current: {contacts[index]['email']}): ") or contacts[index]["email"]
            save_contacts(contacts)
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    
    try: 
        index =int(input("Enter the number of the contact to delete")) -1
        if 0 <= index < len(contacts):
            deleted_contact = contacts.pop(index)
            save_contacts(contacts)
            print(f"Deleted Contact: {deleted_contact['name']}")
        else:
            print("Invalid Contact number")
    except ValueError:
        print("Invalid input. Please Enter another number")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contacts")
        print("4. Delete Contacts")
        print("5. Exit")
        choice = input("Choose an option")
        if choice == "1":
            add_contacts(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting Program")
            break
        else:
            print("Invalid Choice. Choose from choices provided above")

if __name__ == "__main__":
    main()


