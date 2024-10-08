favorite_languages = {
 'jen': 'python',
 'Joe': 'NA',
 'sarah': 'c++',
 'Jack': 'NA',
 'edward': 'rust',
 'phil': 'python',
 'Jim': 'c#',
 'Billy': 'NA',
 'Sam': 'NA',
 }

for name, answer in favorite_languages.items():
    if answer == "NA":
        print(f"{name.title()} still needs to answer the poll.\n")
    else:
        print(f"{name.title()}'s favorite language is {answer.title()}.\n")