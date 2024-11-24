from random import choice
lottery_numbers = [1, 94, 33, 64, 56, 47, 7, 15, 84, 24, "f", "e", "g", "s", "j"]
winning_numbers = []

while len(winning_numbers) < 4:
    new_item = choice(lottery_numbers)
    if new_item not in winning_numbers:
        winning_numbers.append(new_item)
print("Any ticket matching these 4 numbers or letters wins a prize")
print(f"{winning_numbers}")

my_ticket = [33, 7, 24, "e"]

attempts = 0
while True:
    attempts += 1
    random_ticket = []
    while len(random_ticket) < 4:
        new = choice(lottery_numbers)
        if new not in random_ticket:
            random_ticket.append(new)
    if sorted(random_ticket) == sorted(my_ticket):
        break
print(f"It took {attempts} attempts to get a winning ticket.")