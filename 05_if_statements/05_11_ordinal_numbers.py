numbers = range(1, 10)

for i in numbers:
    if int(i) == 1:
        print(f"{i}st")
    if int(i) == 2:
        print(f"{i}nd")
    if int(i) == 3:
        print(f"{i}rd")
    if int(i) >= 4:
        print(f"{i}th")