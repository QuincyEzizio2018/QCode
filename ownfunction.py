# name = input("what's your name? ")
# hello() #this function doesn't exist so we would get an error
# print(name)

"""
def hello():
    print("hello")

name = input("What's your name? ")
hello()
print(name)

"""

#redefine the function
# def hello(to):
#     print("hello,", to)

# name = input("What's your name? ")
# hello(name)

#redefine function to fit when user does not put an arguement
# def hello(to = "World"):
#     print("hello,", to)

# hello()
# name = input("What's your name? ")
# hello(name)

#Rewrite the function to overide the default of functions being at the top of code
def main():
    name = input("What's your name ")
    hello(name)

def hello(to = "world"):
    print("hello,", to)

main()

#Scope means using variables in the defined area