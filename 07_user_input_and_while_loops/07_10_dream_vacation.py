dreamvac = []

while True:
   name = input("What is your name: ")
   spot = input("If you could visit one place in the world, where would you go? ")
   dreamvac.append({"name": name, "spot": spot})
   cont = input("Would you like to let another person take the poll? (Y/N)")
   if cont == "N":
     print ("\n--- Poll Results ---")
     for response in dreamvac: 
        print (f"{response["name"]} wants to go to {response["spot"]}")
     break