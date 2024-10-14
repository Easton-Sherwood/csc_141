while True:
   toppings = input("What toppings do you want on your pizza: ")
   if toppings == 'quit':
     break
   else:
     print(f"I'd love to add {toppings.lower()}!")