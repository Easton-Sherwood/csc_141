current_users = ["Tommy", "Timmy", "Jimmy", "Billy", "Jack"]
new_users = ["Timmy", "Joe", "Bob", "billy", "Duke"]

#This copies the list and makes all variables lowercase
x = 0
for i in current_users:
    current_users[x] = i.lower()
    x +=1


for user in new_users:
    if user.lower() in current_users:
        print ("You will need a new username")
    else:
        print ("This username is available")
