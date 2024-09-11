people = ["Jesus", "Genghis Khan", "Sun Tzu"]
print (f"I would invite {people[0]} to dinner.")
print (f"I would invite {people[1]} to dinner.")
print (f"I would invite {people[2]} to dinner.\n")

print (f"{people[1]} can not attend the dinner\n")

people = ["Jesus", "Sun Tzu", "George Patton"]
print (f"I would invite {people[0]} to dinner.")
print (f"I would invite {people[1]} to dinner.")
print (f"I would invite {people[2]} to dinner.\n")

print("They found a bigger table\n")

people.insert(0, 'Ghandi')
people.insert(2, 'George Washington')
people.append("Thomas Jefferson")

print (f"I would invite {people[0]} to dinner.")
print (f"I would invite {people[1]} to dinner.")
print (f"I would invite {people[2]} to dinner.")
print (f"I would invite {people[3]} to dinner.")
print (f"I would invite {people[4]} to dinner.")
print (f"I would invite {people[5]} to dinner.\n")

print ("The table won't arrive in time, I can only invite 2 people\n")

pop1 = people.pop(5)
pop2 = people.pop(4)
pop3 = people.pop(3)
pop4 = people.pop(2)

print(f"Sorry {pop1}, there is no room at the table for you")
print(f"Sorry {pop2}, there is no room at the table for you")
print(f"Sorry {pop3}, there is no room at the table for you")
print(f"Sorry {pop4}, there is no room at the table for you\n")

del people[1]
del people[0]

print (people)