#All 3 options are in a list
#The for loop will run through each option in the list
#This will allow it to output all 3 options in a single run

alien_color = ['green', 'yellow', 'red']
for i in range(0,3): 
    if alien_color[i] == 'green':
        print("The alien is green! You just earned 5 points!")
    elif alien_color[i] == 'yellow':
        print("The alien is yellow! You just earned 10 points!")
    else:
        print("The alien is red! You just earned 15 points!")

#This is what the original code would look like without the for loop

"""
alien_color == 'green'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")
"""