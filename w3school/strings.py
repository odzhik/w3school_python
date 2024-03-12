# 'hello' is same as "hello"

print("Hello")
print('Hello')

a = "Hello"
print(a)

#You can use three double quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Or three single quotes:

# Example
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!" # H - 0 character, e - First character ...
print(a[1])
print(a[5])

for x in "banana":
  print(x) # b a n a n a 

a = "Kanagattandyrylmagandyktarynyzdan"
print(len(a)) # len - function to show length of a string

#Check string

txt = "Kanagattandyrylmagandyktarynyzdan kan"
print("kan" in txt) # checks word in txt

txt = "Kanagattandyrylmagandyktarynyzdan kan"
if "kan" in txt:
    print("Yes, it is there") # same thing as above

txt = "Kanagattandyrylmagandyktarynyzdan kan"
print("kan" not in txt)

# Slicing
txt = "Kanagattandyrylmagandyktarynyzdan kan"
print(txt[0:7]) # 8th character is not included, output: kanagat
print(txt[:7]) # [0:7] and [:7] same
print(txt[7:]) # [7:] same as [7:30] 
#Negative Indexing
b = "Hello, World!"
print(b[-5:-2]) # orl, -5 character as initial from the end

txt = "Kanagattandyrylmagandyktarynyzdan kan"
print(txt.upper()) # all letters with uppercase KANAGAT.....
print(txt.lower()) # all letters with lowercase
# Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
txt = "          Kanagattandyrylmagandyktarynyzdan kan"
print(txt.strip()) # strip() to remove spaces from beginning till first word Output "Kanagatt...."

#Replace
txt = "Kanagattandyrylmagandyktarynyzdan kan"
print(txt.replace('a', 'o')) # replace all a letters to o 
print(txt.split(" "))

# String Concatenation(combine 2 string to 1)
a = "BMW"
b = "5 series"
print(a + " " +  b)

#Format
age = 20
txt = "I am {} years old" # {} place, where we need to place another data type
print(txt.format(age)) # format(age) turns int into str
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))# with multiple variables
# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Escape Character

# txt = "We are the so-called "Vikings" from the north." incorrect version
txt = "We are the so-called \"Vikings\" from the north."
print(txt)



