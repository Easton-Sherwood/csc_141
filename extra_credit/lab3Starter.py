# Easton Sherwood
# Date: 9/5/2024
# This is the starter file for CSC141 lab day 3

"""
Utilizing your knowledge of python so far...
Come up with a way to print an introduction message
that is specialized with user input

1. You will ensure that you have left 3 comments at the top of your file
    # Your Name
    # Date
    # brief description of what this file does

2. You must prompt the user to supply you their name, age,
    and their major to complete the introduction message

3. You will ensure that the message you print at the end of the file,
    aside from the user input, matches the exact spelling and format of
    the example output that has been provided to you.

4. After completing above 3 steps, remove all comments in this file that are
    not your own and do not forget to rename this file from lab3Starter.py
    to variables.py

"""

print("To generate your introduction, I will need some information from you...")
name = input(f"What is your name? ")
age = int(input(f"What is your age? "))
major = input(f"What is your major? ")
print(f"Hello {name}, you're majoring in {major} before you even turned {age+1}!")



