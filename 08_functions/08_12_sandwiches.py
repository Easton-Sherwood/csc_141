def make_sandwich(*toppings):
   print("\nMaking a pizza with the following toppings:")
   for topping in toppings:
     print(f"- {topping}")

make_sandwich("Pepperoni")
make_sandwich("Pepperoni", "Extra Cheese", "Meatballs")
make_sandwich("Pepperoni", "Jalepenos", "Beef", "Meatballs", "Buffalo Sauce")