class Contact:
    phone_directory = []

    def __init__(self, name, phone_number):
        self.name = name
        self.phone = phone_number
        Contact.phone_directory.append(self)

    def show_contact(self):
        return f"Name: {self.name}, Phone Number: {self.phone}"

    @classmethod
    def show_all_contacts(cls):
        if len(cls.phone_directory) == 0:
            print("No contacts in the phone book.")
        else:
            print("All Contacts from the Phone Book:")
            for contact in cls.phone_directory:
                print(contact.show_contact())
    
    
    @classmethod
    def search_contact(cls, search_name):
        for contact in cls.phone_directory:
            if contact.name.lower() == search_name.lower():
                return contact.phone
        return f"Contact not found for {search_name}."
    @staticmethod
    def validate_phone_number(phone_number):
        if len(phone_number) >= 8 and phone_number.isdigit():
            return True
        else:
            return False

n_contacts = int(input("Enter the number of contacts you want to add: "))
for _ in range(n_contacts):
    name = input("Enter contact name: ")
    phone_number = input("Enter contact phone number: ")
    if Contact.validate_phone_number(phone_number):
        Contact(name, phone_number)
    else:
        print(f"Invalid phone number for {name}. Phone number should be at least 8 digits long and contain only numbers.")

# c1 = Contact("Alice", "123-456-7890")
# c2 = Contact("Bob", "987-654-3210") 
# c3 = Contact("Charlie", "555-555-5555")
# print(c1.show_contact())
# print(c2.show_contact())
# print(c3.show_contact())

Contact.show_all_contacts()
# print(Contact.search_contact("Alice"))
# print(Contact.search_contact("David"))