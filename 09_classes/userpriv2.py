from userpriv1 import User
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
