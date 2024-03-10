#Creating Variables

x = 5
y = "John"
print(x)
print(y)

#You can rewrite a value of 1 variable like this
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Casting
#If you want to specify the data type of a variable, this can be done with casting.

x = str(4) # x will be '4'
y = int(5) #y will be 5
z = float(3) #z will be 3.0

#Variable Names

Varname = "Hello, world!"
Var_name = "Hello, world!"
_Var_name = "Hello, world!"
varName = "Hello, world"
VARNAME = "Hello, world!"
varname2 = "Hello, world!"
print(VARNAME)

# Illegal
"""
2varname = "Hello, world!"
var-mame = "Hello, world!"
var name = "Hello, world"
"""

#Techniques to read more simply var names

#Camel case

myVariableName = "Hello, world!" #each new word with capital letter except first word

#Pascal case

MyVariableName = "Hello, world!" #each new word with capital letter

#Snake case

my_variable_name = "Hello, world!" #each new word separated by an _ underscore

#Assign Multiple Values

x, y, z = "Orange", "Banana", "Apple"
print(x, y, z) # Orange Banana Apple

x = y = z = "Orange"
print(x, y, z) #Orange Orange Orange

#Unoack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x, y, z) # apple, banana, cherry

x = "Hello "
y = "World"
z = "!"
print(x + y + z) # Hello Wolrd!

x = 10 
y = 5
print(x + y) # 15

x = 5
y = "Olzhas"
print(x, y)

#Global variables

# Variables that are created outside of a function (as in all of the examples above) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#If you create a variable with the same name inside a function, this variable will be local, 
#and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()# Python is fantastic

print("Python is " + x)# Python is awesome

# To create a global variable inside a function, you can use the global keyword.

def myfunc():
  global x 
  x = "awesome"

myfunc() 

print(x) # awesome

#Also, use the global keyword if you want to change a global variable inside a function.

x = "awesome"

def myfunc():
  global x 
  x = "fantastic"

myfunc()

print(x) #fantastic






