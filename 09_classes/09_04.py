class Restaurant:

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0
    def describe_restaurant(self):
        print(f"The restaurants name is: {self.name}")
        print(f"The restaurant serves: {self.cuisine}")    
    def open(self):
        print(f"{self.name} is now open.")
    def served(self):
        print(f"The restaurant has served {self.number_served} guests.")

food = Restaurant('Five Guys', 'Burgers')
food.served()

food.number_served = 13
food.served()
