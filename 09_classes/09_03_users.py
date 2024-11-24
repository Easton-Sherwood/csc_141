class user:

    def __init__(self, first_name, last_name, dob, height, state_of_residence):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.state_of_residence = state_of_residence
        self.height = height
    def describe_user(self):
        print(f"The users full name is {self.first_name} {self.last_name}. They were born on {self.dob}. They are {self.height} tall and live in {self.state_of_residence}.")
    def greet_user(self):
        print(f"Welcome {self.first_name}, we have been expecting you.")

person = user('Jack', 'Daniels', "05/24/1995", "5'11", "Texas")
person.describe_user()
person.greet_user()
print("\n")

person = user('Jimmy', 'Johns', "09/13/1987", "5'7", "Oklahoma")
person.describe_user()
person.greet_user()
print("\n")

person = user('Jimmy', 'Space', "01/01/0001", "10'9", "Maryland")
person.describe_user()
person.greet_user()
print("\n")