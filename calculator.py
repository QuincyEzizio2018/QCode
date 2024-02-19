
"""
Integer (int)
+
-
*
/
% Modulus (Returning a dividend)
"""

# x = 1
# y = 2

# z = x + y

# print(z)

# x = int(input("What is X "))
# y = int(input("What is Y "))

# print(x + y) 

# z = x + y 
# print(z)  this returns 12 because the + is serving as a concatenation

# z = int(x) + int(y) #this converts the string values to integer
# print(z) 

#the complicated one line code (This has put to null our readability and simplicity in coding)
#print(int(input("What is X ")) + int(input("What is Y ")))


"""
FLOAT (float)
"""
# x = float(input("What is X "))
# y = float(input("What is Y "))

# print(x + y) 

#docs.python.org/3/library/functions.html#round
#round(number[, ndigits])   [] means optional  ndigit means number of digits to round to
# x = float(input("What is X "))
# y = float(input("What is Y "))
# z = round(x + y)
# print(z) 

# #format the integer to have a separator like 1,000
# print(f"{z:,}")

"""
DIVISION (/)
"""
x = float(input("What is X "))
y = float(input("What is Y "))
z = round(x/y, 2) 
#print(z) #or 
print(f"{z:.2f}")