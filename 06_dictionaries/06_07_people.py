person1 = {"first_name": "Easton", "last_name": "Sherwood", "city": "Damascus"}
person2 = {"first_name": "Jimmy", "last_name": "John", "city": "Clarksburg"}
person3 = {"first_name": "Joe", "last_name": "Baptiste", "city": "Reading"}

persons = [person1, person2, person3]
for person in persons:
    print (f'My name is {person["first_name"]} {person["last_name"]} and I live in {person["city"]}')