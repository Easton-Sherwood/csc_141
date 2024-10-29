sandwich_orders = ["Italian", "BLT", "BBQ", "Tuna", "Ham and Cheese"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"We just made a {sandwich} sandwich!")
    finished_sandwiches.append(sandwich)

print (f"Here is the list of finished sandwiches {finished_sandwiches}")

print (f"Here is the list of finished sandwiches {sandwich_orders}")