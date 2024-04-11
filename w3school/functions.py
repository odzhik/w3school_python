# def new_function(): # функция не запустится пока ее не вызвать
#     print("hello from a function!")

# new_function() # чтобы вызвать функцию 

# def my_function(fname):
#     print(fname + " Zhakayev")

# my_function("Olzhas")
# my_function("Zhalgas")

# def my_family(name, sname):
#     print(name + " " + sname)

# my_family("Olzhas", "Zhakayev")  # Here are right arguments
# my_family("Zhalgas", "Zhakayev")
# my_family("Aigul", "Zhakayeva")
# my_family("Leila", "Zhakayeva")
# my_family("Didara", "Zhakayeva")

# my_family("Olzhas") # incorrect, cause only 1 argument

# def new_function(*cars):
#     print("I have " + cars[0]) # we cant write *cars for full tuple, bcs "I have" is string and we cant combine

# new_function("BMW")

# def cars(car1, car2, car3):
#     print("I drive " + car1)
#     print("Otegen drive " + car2)
#     print("Talan drive " + car3)

# cars(car1 = "Camry 30", car2 = "BMW x5", car3 = "Aristo")

# def my_func(**kid):
#     print("His last name is " + kid["name"])

# my_func(sname = "Parker", name = "Peter")

# def my_country(country = "Norway"): # default value = Norway
#     print("I am from " + country)
# my_country("Kazakhstan")
# my_country("USA")
# my_country()

# def my_food(food):
#     for x in food:
#         print(x)

# fruits = ["apple", "banana", "cherry"]

# my_food(fruits)

# def my_func(x):
#     return x * 5

# print(my_func(5))
# print(my_func(10))

def new_func():
    pass

# def my_func(x, /):
#     print(x)

# my_func(4)

# def my_func(*, x):
#     print(x)

# my_func(x = 4)

# def my_func(a, b, /, *, c, d): # / что до этого знака это positional only, то что после * keyword only
#     print(a + b + c + d)

# my_func(5, 6, c = 7, d = 8)

# RECURSION

def tri_rec(k):
    if(k > 0):
        result = k + tri_rec(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_rec(6)