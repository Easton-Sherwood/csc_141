river = {
 "Nile River": "Egypt",
 "Mississippi River": "Mississippi",
 "Rio Grande River": "Colorado",
 }

for name, place in river.items():
    print(f"The {name.title()} runs through {place.title()}.\n")