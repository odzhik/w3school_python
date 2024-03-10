# 3 numeric types
"""
int, float, complex
"""

# int is negative, positive, whole number
x = 1
y = -1
z = 3484758475845
print(type(x)) #int
print(type(y)) #int
print(type(z)) #int

#float is neg,pos containing decimals like 0.9 or 0.6 etc
x = 1.10
y = 1.0
z = -59.90
print(type(x))
print(type(y))
print(type(z))

# Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 3e2 # 3 * 10^2 = 300.0
print(x) # 300
print(type(x)) 
y = -2e3 # -2 * 10^3 = -2000.0
print(y)

#Complex 
# Complex numbers are written with a "j" as the imaginary part:
x = 3 + 5j
print(x) # 3+5j
# You can convert from one type to another with the int(), float(), and complex() methods:
x = 1 # it is int
a = float(x) # now int is float, 1.0
print(a) #1.0

c = complex(x)
print(c) # 1 + 0j

import random # built in module to make random numbers
print(random.randrange(1,100)) # some random num

x = 5.5
a = int(x)
print(a) # 5
x = 5.9
a = int(x)
print(a) #5
