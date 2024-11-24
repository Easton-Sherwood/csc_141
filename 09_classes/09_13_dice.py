from random import randint

class dice:
    def __init__(self, faces, spins):
        self.faces = int(faces)
        self.spins = int(spins)
    def roll_die(self):
        print (f"You rolled a d{self.faces}!")
        for i in range(self.spins):
            roll = randint(1, self.faces)
            print (f"You rolled a {roll}")

d6 = dice(6, 10)
d6.roll_die()

d10 = dice(10, 10)
d10.roll_die()

d20 = dice(20, 10)
d20.roll_die()