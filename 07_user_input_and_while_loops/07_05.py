while True:
     age = input("How old are you: ")
     if age == 'quit':
         break
     elif int(age) < 3:
        print(f"The ticket is free!")
     elif int(age) >= 3 and int(age) <= 12:
        print(f"The ticket is $10!")
     elif int(age) > 12:
        print(f"The ticket is $15!")