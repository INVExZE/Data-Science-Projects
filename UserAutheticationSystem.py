'''Access Modifiers
Project: User Authentication System

Description: Implement a basic user authentication system.
Features: Private attributes for storing user passwords.
Public methods for registering and authenticating users.
Protected methods for password encryption.'''

class UserAuthenticationSystem:
    def __init__(self):
        self.users = {}  

    def register(self, username, password):
        if username in self.users:
            print("Username already exists. Please choose a different username.")
        else:
            self.users[username] = password
            print(f"User '{username}' registered successfully.")

    def authenticate(self, username, password):
        if username in self.users and self.users[username] == password:
            print(f"User '{username}' Authenticated successfully.")
            return True
        else:
            print(f"User '{username}' Authentication failed. Incorrect username or password.")
            return False

# Example usage
auth = UserAuthenticationSystem()
print("\n-----------------------------------------")

auth.register("Sanjay", "password123")
auth.register("Ankit", "mypassword")
auth.register("Ayush", "mypas456sword")
auth.register("Aakash", "my1232password")

print("\n-----------------------------------------")

# Attempt to authenticate users
auth.authenticate("Sanjay", "password123")  # Should succeed
auth.authenticate("Ankit", "wrongpassword")  # Should fail
auth.authenticate("Ayush", "password123")  # Should fail

print("\n-----------------------------------------")
