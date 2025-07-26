def show_menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    
    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone},{email}\n")
    
    print("Contact added successfully!")

def view_contacts():
    print("\n--- All Contacts ---")
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("No contacts found.")
            for contact in contacts:
                name, phone, email = contact.strip().split(",")
                print(f"Name: {name}, Phone: {phone}, Email: {email}")
    except FileNotFoundError:
        print("No contacts file found.")

def search_contact():
    search_name = input("Enter name to search: ").lower()
    found = False
    try:
        with open("contacts.txt", "r") as file:
            for contact in file:
                name, phone, email = contact.strip().split(",")
                if search_name in name.lower():
                    print(f"Found: Name: {name}, Phone: {phone}, Email: {email}")
                    found = True
        if not found:
            print("Contact not found.")
    except FileNotFoundError:
        print("No contacts file found.")

# Main program loop
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
