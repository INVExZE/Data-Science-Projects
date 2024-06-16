'''Classes and Objects

Project: Contact Management System

Description: Create a system to manage contact information.
Features: Class Contact with attributes like name, phone number, and email.
Methods to add, update, and display contacts.'''

class Contact:
    def __init__(self, name, number, email):
        self.name = name 
        self.phoneNumber = number
        self.email = email

    def display(self):
        print(f" {self.name} : {self.phoneNumber} : {self.email}")

class Manager:
    def __init__(self):
        self.contacts = []

    def add(self, name, number, email):
        contact = Contact(name, number, email)
        self.contacts.append(contact)

    def update(self, name, newName = None, newNumber = None, newEmail = None ):
        for contact in self.contacts:
            if contact.name == name:
                if newName:
                    contact.name = newName
                if newNumber:
                    contact.phoneNumber = newNumber
                if newEmail:
                    contact.email = newEmail
                break

    def display(self):
        for contact in self.contacts:
            contact.display()


manager = Manager()

manager.add('Ayush', '123XXX7890', 'ayush@gmail.com')
manager.add('Ankit', '9XXXX43210', 'ankit@gamil.com')
manager.add('Sanjay', '9876XX3210', 'sanjay@gamil.com')
manager.add('Bablu', '9876543210', 'bablu@gamil.com')

line1 = "-------------------------------------------------------------"
print(line1)
print("The Name and Number of all Contacts are :\n")
manager.display()

manager.update('Ayush', newNumber = '1112223333')

print(line1)
print("Contacts after update:\n")
manager.display()
print(line1)       

        
    