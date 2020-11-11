import functions

def main():
    contactBook = functions.Contacts()
    option = ""
    while option != "0":
        print("""
            === === === === ===
            Python Contact Book
            === === === === ===
            
            0. Quit program
            1. Add contact
            2. Remove contact
            3. Search for contact
            4. View all contacts
            5. Sort by first name
            6. Sort by last name
        """)
        option = input()
        if option == "1": # Add
            firstName = input("First Name: ")
            lastName = input("Last Name: ")
            phoneNumber = input("Phone Number: ")
            address = input("Address: ")
            contactBook.add(firstName, lastName, phoneNumber, address)
        elif option == "2": # Remove
            if contactBook.n == 0:
                print("The contact book is empty.")
            else:
                name = input("Enter the name you would like to remove from the book:")
                contactBook.remove(name)
        elif option == "3": # Search
            if contactBook.s == 1:
                name=input("Enter first name: ")
                contactBook.search(name)
            else:
                name = input("Enter first name: ")
                contactBook.search(name)
        elif option == "4": # View
            contactBook.view()
        elif option == "5": # Sort by first name
            contactBook.sortByFirst()
        elif option == "6": # Sort by last name
            contactBook.sortByLast()

if __name__ == '__main__':
    main()