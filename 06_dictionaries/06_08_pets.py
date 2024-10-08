pet1 = {"breed": "Golden Lab", "name": "Luke", "city": "Damascus"}
pet2 = {"breed": "Bulldog", "name": "Bella", "city": "Frederick"}
pet3 = {"breed": "German Shepherd", "name": "Skyla", "city": "Woodfield"}

pets = [pet1, pet2, pet3]
for pet in pets:
    print (f'My friends name is {pet["name"]}, they have a {pet["breed"]} and they live in {pet["city"]}')