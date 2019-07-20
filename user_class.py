
class User:
    # Identifies following parameters
    def __init__(self, name, email, password, age):
        self.name = name
        self.email = email
        self.password = password
        self.age = age
        self.mood = "Happy"
        
    # Print mood statement
    def status_update(self):
        print("I'm feeling " + self.mood + " today.")
    
    # Change Password function   
    def change_password(self, old_password, new_password):
        if old_password == self.password:
            self.password = input("New Password: ")
            print("Password successfully changed :D")
            print("Your new password is " + self.password)
        elif old_password != old_password:
            print("The password you entered doesn't match the password we have registered in the system.")
        else:
            print("Enter a password")
