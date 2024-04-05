# Dictionaries are used to store data values in key:value pairs.

#ordered, chanchagle not duplicated

car = {
    "brand": "Ford",
    "model": "Mustang", 
    "year": 1964
}
# print(car)
# print(car["brand"])
# print(len(car))

# USA = car["brand"]
# print(USA)

# x = car.keys()
# print(x)

# car["color"] = "black"
# car.update({"color": "white"})
# print(x)
# print(car)

# y = car.values() # значение внутри переменных
# print(y)

# z = car.items() # пара, ex: brand: Ford, model: Mustang ...
# print(z)

# if "model" in car:
#     print('Yes')
# else:
#     print("No")

# car["year"] = "2024"
# print(car)

# car.update({"brand": "Dodge"})
# car.update({"model": "Challenger"})
# print(car)

# car["color"] = "Black"
# print(car)

# car.pop("color")
# print(car)

# car.popitem() # delete last pair
# print(car)

# del car["model"] # del is used to delete specified pair that you choose
# print(car)

# # del car
# # print(car) # will cause error because there is no dict now

# car.clear()
# print(car)

car = {
    "country": "Italy",
    "Name": "Ferrari",
    "model": "458 Italia",
    "year": 2014,
    "mileage": "30000 km"
}

# for x in car:
#     print(x) # output will be : country, name, model, year, mileage


# for x in car:
#     print(car[x]) # return values of keys

# for x in car.values():
#     print(x) # same as previous method

# for x, y in car.items():
#     print(x, y) # return both keys and values

# newcar = car.copy()
# print(newcar) # for copy a dict

# copycar = dict(car) # same as previous
# print(copycar)

# NESTED DICTIONARIES

myFamily = {
    "Father": {
        "name" : "Zhalgas",
        "birthday": 1964
    },
    "Sister": {
        "Name": "Leyla",
        "birthday": 1991
    },
    "Mother":{
        "name": "Aigul",
        "birthday": 1969
    }
}

# print(myFamily)


car1 = {
    "Country": "Germany",
    "Name": "Porsche"
}

car2 = {
    "Country": "USA",
    "Name": "Chevrolet"
}

car3 = {
    "Country": "Korea",
    "Name": "Hyundai"
}

cars = {
    "car1": car1,
    "car2": car2,
    "car3": car3
}

print(cars)

print(cars["car1"]["Name"])
