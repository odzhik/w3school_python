# def myfunc():
#     x = 300
#     def insidefunc():
#         print(x)
#     insidefunc()

# myfunc()

# a = 100

# def myfunc():
#     print(a)

# myfunc()
# print(a)

# x = 100

# def myfunc():
#     x = 200
#     print(x) # 200

# myfunc()# 200 
# print(x)# 100

x = 100

def myfunc():
    global x
    x = 300

myfunc()

print(x)# 300

