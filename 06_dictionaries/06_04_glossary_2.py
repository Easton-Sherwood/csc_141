favorite_num = {
 "Comment": "to exclude lines from being read as code",
 "Integer": "to save a numerical value",
 "String": "to save a string of characters",
 "List": "as a group of variables or values",
 "Tuple": "as an unmutable list",
 "If statement": "to run code if a condition is met",
 "If else statement": "for multiple different conditions to give different outputs",
 "For loop": "to repeat code for a fixed number of times",
 "While loop": "to repeat code until a condition is met",
 "Dictionary": "to store keywords along with values associated with those keywords",
 }

for name, define in favorite_num.items():
    print(f"A {name.title()} is used {define.lower()}.\n")