'''
> repr Greater than
>= repr Greater than equal to
< repr Less than
<= repr Less than equal to
== repr Equality comparing the thing on the left and right
= repr Assignment copying the thing on the right to the left
!= repr Not-Equal to some value next to it
'''

#compare.py
'''
The keyword If
We use "If" to ask questions in python or programming
'''
# x = int(input("What's x? "))
# y = int(input("What's y? "))

# if x < y: #x < y : this expression is a boolean expression with either a Yes(True) or No(False) answers
#     print("x is less than y")
# if x > y:
#     print("x is greater than y")
# #x = y assigns y to x but x==y compares the values of x and y
# if x == y:
#     print("x is equal to y")

'''
from the Straight Long diagram we see Starts, ask the question, move right fortrue(which prints or perform operation),
move left for false(which does nothing) but ask next question till Stop.
We can decode or note that we keep asking this three question
even after getting the answer at first run which makes the code REPEATITIVE
'''

#We introduce "elif" which is else if to make the code more concise or running time lesser
'''
from now fat diagram we see Starts, ask the first question which if true,move right, perform operation(print) and stop, but
if false, move left for the next question which if true, performs operation and stop without having to run or go through all questions.

from the diagram since we are using only elif we tend to add false to the last question or statement which also leads to stop to break out of the question sessions.
'''
# x = int(input("What's x? "))
# y = int(input("What's y? "))

# if x < y: #x < y : this expression is a boolean expression with either a Yes(True) or No(False) answers
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# #x = y assigns y to x but x==y compares the values of x and y
# elif x == y:
#     print("x is equal to y")

#We introduce "else" which is else if to make the code more concise or running time lesser
'''
from the concise diagram we see Starts, since we have only 3 questions we can use "if" for the first, "elif" for the second and "else" for any other thing
'''
# x = int(input("What's x? "))
# y = int(input("What's y? "))

# if x < y: #x < y : this expression is a boolean expression with either a Yes(True) or No(False) answers
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# #x = y assigns y to x but x==y compares the values of x and y
# else:
#     print("x is equal to y")

"""
The difference in the diagram is the it gets smaller with fewer nodes and blocks
Simplicity, Readability are achieved using this
"""

#Using "Or" to rewrite the same code for conscise coding
# x = int(input("What's x? "))
# y = int(input("What's y? "))

# if x < y or x > y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")

'''
from the concise diagram we see Starts, since we have only 2 questions we can use "if" for the first, "else" for any other thing
'''


#Using "!=" to rewrite the same code for more conscise coding
# x = int(input("What's x? "))
# y = int(input("What's y? "))

# if x != y:
#     print("x is equal to y")
# else:
#     print("x is not equal to y")

'''
We get a more concise diagram we see Starts, Question, True and False all leads to operation(print) and stop
'''

'''
"Indentation" and "Colon" are neccessary
'''



#grade.py which give the grade of student scores
# score = int(input("Score: "))

# if score >= 90 and score <= 100:
#     print("Grade: A")
# elif score >= 80 and score < 90:
#     print("Grade: B")
# elif score >= 70 and score < 80:
#     print("Grade: C")
# elif score >= 60 and score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")

#Let tigthen up the code or make it concise watch out the "90<= Score <=100" or "60<= Score <70"
# score = int(input("Score: "))

# if 90 <= score <= 100:
#     print("Grade: A")
# elif 80 <= score < 90:
#     print("Grade: B")
# elif 70 <= score < 80:
#     print("Grade: C")
# elif 60 <= score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")


#Let tigthen up the code or make it more concise by removing the comparison of the lower to upper bound.
# score = int(input("Score: "))

# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")



#parity.py (check for odd or even number) using % modulus
# x = int(input("What's x? "))

# #Even numbers are numbers divisible by 2
# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


#Rewriting parity.py with functions
# def main():
#     x = int(input("What's x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")

# def is_even(n):
#     if n % 2 == 0  #Bool can only return 2 values True or False and first letter must be Capital
#         return True
#     else:
#         return False

# main()

#Rewriting the functions more concisely
# def main():
#     x = int(input("What's x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")

# def is_even(n):
#     return True if n % 2 == 0 else False

# main()

#Rewriting the functions much more concisely
# def main():
#     x = int(input("What's x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")

# def is_even(n):
#     return n % 2 == 0

# main()

#house.py : prompt the user for their name and print the house they are in, in the world of harrypotter
# name = input("What's your name? ")
# if name == "Harry":
#     print("Gryffindor")
# elif name == "Hermione":
#     print("Gryffindor")
# elif name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")


#Rewriting house.py : concise
# name = input("What's your name? ")
# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")


#Rewriting house.py : more concise using "match"
# name = input("What's your name? ")
# match name:
#     case "Harry":
#         print("Gryffindor")
#     case "Hermione":
#         print("Gryffindor")
#     case "Ron":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who?")

#Rewriting house.py : more concise using "match"
name = input("What's your name? ")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
