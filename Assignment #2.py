import csv
#Assignment-2 Lakshmi Urjitha Dhadigam 1223270

# a file in the current directory

FILENAME = "contacts.csv"

def write_contacts(contacts):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)   

def read_contacts():
    contacts = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            contacts.append(row)
    return contacts

def list_contacts(contacts):
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact[0]} ")
    print()
    
def view_contacts(contacts):
    number = int(input("Number : "))
    name = input("Name : ")
    email = input("Email: ")
    phone = input("Phone: ")
    print()
   
def add_contacts(contacts):
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone:")
    contact = [name, email, phone]
    contacts.append(contact)
    write_contacts(contacts)
    print(f"{name} was added.\n")

def delete_contacts(contacts):
    index = int(input("Number: "))
    if index < 1 or index > len(contacts):
        print("Invalid  number.\n")
    else:
        contact = contacts.pop(index - 1)
        write_contacts(contacts)
        print(f"{contact[index]} was deleted.\n")    
        
def display_menu():
    print("Contact Manager")
    print()
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view – View a contact")
    print("add -  Add a contact")
    print("del -  Delete a contact")
    print("exit - Exit program")
    print()

def main():
    display_menu()
    contacts = read_contacts()
    while True:        
        command = input("Command: ")
        if command.lower() == "list":
            list_contacts(contacts)
        elif command.lower() =="view":
            view_contacts(contacts)
        elif command.lower() == "add":
            add_contacts(contacts)
        elif command.lower() == "del":
            delete_contacts(contacts)       
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
