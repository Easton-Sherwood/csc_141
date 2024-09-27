numbers = range(1, 10)

for i in numbers:
    if int(i) == 1:
        print(f"{i}st")
    elif int(i) == 2:
        print(f"{i}nd")
    elif int(i) == 3:
        print(f"{i}rd")
    else:
        print(f"{i}th")