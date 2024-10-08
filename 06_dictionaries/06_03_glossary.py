favorite_num = {
 "Comment": "to exclude from being read as code",
 "For loop": "to repeat code for a fixed number of times",
 "If statement": "to run code if a condition is met",
 "Dictionary": "to store keywords along with values associated with those keywords",
 "Tuple": "As an unmutable list",
 }

for name, define in favorite_num.items():
    print(f"A {name.title()} is used {define.lower()}.\n")