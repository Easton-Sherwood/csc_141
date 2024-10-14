sandwich_orders = ["Italian", "Pastrami", "BLT", "Pastrami", "BBQ", "Tuna", "Pastrami", "Ham and Cheese"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich == "Pastrami":
        print ("We are out of Pastrami")
    else:
        print(f"We just made a {sandwich} sandwich!")
        finished_sandwiches.append(sandwich)

print (f"Here is the list of finished sandwiches {finished_sandwiches}")