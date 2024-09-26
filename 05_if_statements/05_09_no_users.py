users = []


if users:
    for user in users:
        if user == "admin":
            print("hello admin, do you need a status report?")
        else:
            print(f"welcome back {user}, glad to see you logging in again.")
else:
    print ("WE NEED TO FIND SOME USERS!")
