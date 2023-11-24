names = []
phone_numbers = []
emails = []
addresses = []

while True:
    print("\nContact Book\n\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
    ch = input("Enter your choice: ")

    if ch == '1':
        name = input("Name: ")
        phone_number = int(input("Phone Number: "))
        email = input("Email: ")
        address = input("Address: ")

        names.append(name)
        phone_numbers.append(phone_number)
        emails.append(email)
        addresses.append(address)
        print("\nContact added successfully.")
        
    elif ch == '2':
        print("\nName\t\t\t\tPhone Number")
        for i in range(len(names)):
            print("{:<20}\t\t{}".format(names[i], phone_numbers[i]))



    elif ch == '3':
        search_term = input("\nEnter the name to search: ")
        print("\nSearch result:\n")
        found = False
        for i in range(len(names)):
            if search_term == names[i]:
                found = True
                print("Name: {}\tPhone Number: {}".format(names[i], phone_numbers[i]))
                break
        if not found:
            print("\nName Not Found")

    elif ch == '4':
        update = input("\nEnter the name to update: ")
        if update in names:
            index = names.index(update)
            new_name = input("Enter new name: ")
            names[index] = new_name
            new_phone_number = input("Enter new phone number: ")
            phone_numbers[index] = new_phone_number
            new_email = input("Enter new email: ")
            emails[index] = new_email
            new_address = input("Enter new address: ")
            addresses[index] = new_address
            print("\nContact updated successfully.")
    elif ch == '5':
        delete_name = input("\nEnter the name to delete: ")
        if delete_name in names:
            index = names.index(delete_name)
            del names[index]
            del phone_numbers[index]
            del emails[index]
            del addresses[index]
            print("\nContact deleted successfully.")
        else:
            print("\nName Not Found")
    elif ch == '6':
        print("\nExiting Contact Book. Goodbye!")
        break
    else:
        print("\nInvalid choice. Please enter the choice correctly.")

