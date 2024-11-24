from random import choice
lottery_numbers = [1, 94, 33, 64, 56, 47, 7, 15, 84, 24, "f", "e", "g", "s", "j"]
winning_numbers = []

def new_ticket():
    while len(winning_numbers) < 4:
        new_item = choice(lottery_numbers)
        if new_item not in winning_numbers:
            winning_numbers.append(new_item)

new_ticket()
print("Any ticket matching these 4 numbers or letters wins a prize")
print(f"{winning_numbers}")