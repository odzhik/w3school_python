# class MyClass:
#     x = 5

# p1 = MyClass()
# print(p1.x)

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#             return f"{self.name}({self.age})"

# p1 = person("Olzhas", 20)

# # print(p1.name)
# # print(p1.age)

# print(p1)

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = person("Olzhas", 20)
p1.myfunc()
p1.name = "Artoty"
p1.myfunc()

del p1