class User:
    def __init__(self, first_name, last_name, dob, height, state_of_residence):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.state_of_residence = state_of_residence
        self.height = height
        self.login_attempts = 0
    def describe_user(self):
        print(f"The users full name is {self.first_name} {self.last_name}. They were born on {self.dob}. They are {self.height} tall and live in {self.state_of_residence}.")
    def greet_user(self):
        print(f"Welcome {self.first_name}, we have been expecting you.")
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Login attempts made: {self.login_attempts}")
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"The number of login attempts has been reset to {self.login_attempts}")

class Privileges:
    def __init__(self):
        self.privileges = "Can add post", "Can delete post", "Can ban user"
    def show_privileges(self):
        privileges_string = ', '.join(self.privileges)
        print(f"Here is a list of admin privileges: {privileges_string}")


class Administrator(User):
    def __init__(self, first_name, last_name, dob, height, state_of_residence):
        super().__init__(first_name, last_name, dob, height, state_of_residence)
        self.privileges = Privileges()

person = Administrator('Jimmy', 'Johns', "09/13/1987", "5'7", "Oklahoma")
person.privileges.show_privileges()