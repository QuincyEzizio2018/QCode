"""
Function
Side effect is the print out
Debugging is noting fixing code error
variable : A container to return a value or for re-use purposes.
Comment (# for single line, """"""" for block code)
Pseudocode : Todo list

"""
"""
STRING (string)
docs.python.org/3/library/stdtypes.html#string-methods

"""
#Ask user for their name
#name = input("What's your name? ")

#Say hello to user
#This accepts input but prints the stated strings even if the input is not Jamiu
#print("hello, Jamiu") 

"""print("hello, ")
print("Jamiu") 
"""

#This displays the inputted value but on a different line
"""print("hello, ")
print(name) 
"""
# #This displays the inputted value on same line Solution 1
# print("hello, " + name)

'''
#Documentation : Program Documentations have the answers to our questions if we look deeply
#Accessing python "print function" documentation online visit : docs.python.org/3/library/functions.html/print

print(*objects,sep=' ', end='\n', file=sys.stdout, flush=false)
1. the "print" is the function 
the open and closed bracket() : everything enclosed is called the potential Parameters to the functions or arguement of the function
Parameters (What you can pass to the function or input to the functions) : What the function can take
Arguements (Using the function and passing or inputting the values into the paranthesis) : Values you are passing to the function.

2. * means any numbers of ... *Object means any number of objects

 3. Sep=' ', Separation and takes the value of space : hence multiple arguement in the print function is separated by space.

4. end='\n',  ends a print statement and move it to the next line.

'''

#This displays the inputted value on same line Solution 2
# print("hello, ", end = "")
# print(name) 

#we just overide the separation statement to have no space in between and we can solve this by adding the space after hello,
#print("hello,", name, sep = "") 

# #Assumming we want to print Hello "Friend"
# print ('hello "Friend"') # Using the single quote can help print the double quote
# print ("Hello \"Friend\"") # using escaping (\) at the begining of the quote and at the end of text before the last quote mark

#Remove whitespace from string (if we input         Jame            it will print hello          jame        )
#name = name.strip() #this removes the users extra's white spaces. 

#Capitalize user's name
#name = name.title()

#Remove whitespace from string and capitalize
#name = name.strip().title()

#Let's redo the code for restructuring and code optimization
name = input("What's your name? ").strip().title()

#Split inputed strings with space.
first, last = name.split(" ")

#Format string
print(f"hello, {first}") #This prints the first name after splitting

