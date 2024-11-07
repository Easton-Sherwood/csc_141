class Restaurant:

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    def describe_restaurant(self):
        print(f"The restaurants name is: {self.name}")
        print(f"The restaurant serves: {self.cuisine}")    
    def open(self):
        print(f"{self.name} is now open.")


food = Restaurant('Five Guys', 'Burgers')

food.open()
food.describe_restaurant()
