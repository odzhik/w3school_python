#Data types
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

x = 5
print(type(x)) # class int (type() command gives a data type of variable)
x = 5.0
print(type(x)) # class float
x = range(6)
print(type(x))#class range
x = True
print(type(x)) #class bool

# If you want to specify the data type, you can use the following constructor functions:

x = str("Hello")
print(x) # Hello

x = float(5)
print(type(x)) # class float



