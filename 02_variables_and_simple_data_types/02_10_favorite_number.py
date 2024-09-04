number = int(7)
#The question variable will display the original favorite number and then
#it will ask for the users favorite number
question = int(input(f"My favorite number is {number}, what is yours? "))
#It will compare the inputted number to the original number and 
#display a response depending on the answer
if question>number:
    print ("Your favorite number is more than mine")
else:
    print ("Your favorite number is less than mine")