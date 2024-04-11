# def new_function(): # функция не запустится пока ее не вызвать
#     print("hello from a function!")

# new_function() # чтобы вызвать функцию 

# def my_function(fname):
#     print(fname + " Zhakayev")

# my_function("Olzhas")
# my_function("Zhalgas")

def my_family(name, sname):
    print(name + " " + sname)

# my_family("Olzhas", "Zhakayev")  # Here are right arguments
# my_family("Zhalgas", "Zhakayev")
# my_family("Aigul", "Zhakayeva")
# my_family("Leila", "Zhakayeva")
# my_family("Didara", "Zhakayeva")

# my_family("Olzhas") # incorrect, cause only 1 argument

def new_function(*cars):
    print("I have " + cars[0]) # we cant write *cars for full tuple, bcs "I have" is string and we cant combine

new_function("BMW")

def cars(car1, car2, car3):
    print("I drive " + car1)
    print("Otegen drive " + car2)
    print("Talan drive " + car3)

cars(car1 = "Camry 30", car2 = "BMW x5", car3 = "Aristo")




