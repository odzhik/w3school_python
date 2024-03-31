# cars = ("BMW", "Mercedes", "Audi", "Porsche", "Volkswagen")
# print(cars)
# print(len(cars))

# thistuple = ("apple",)
# print(type(thistuple))

# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)
# tuple4 = ("abc", 34, True, 40, "male")

# print(type(tuple2))

# print(cars[2])
# print(cars[-1])
# print(cars[0:3])
# print(cars[0:])
# print(cars[:6])
# print(cars[-5:-1])

# cars = ("Volvo", "Saab", "Lotus")
# x = list(cars)
# x[1] = "Ferrari"
# print(x)

# x.append("Lamborgini") # to add
# print(x)

# x.remove("Lotus")# to del something
# print(x)

# # del x
# # print(x) # complete delete list

# UNPACKING
 
# countries = ("Italy", "Germany", "USA") # this is packing, when we assign value
# (pizza, beer, burger) = countries # this is unpacking
# print(pizza)
# print(beer)
# print(burger)

countries = ("France", "Russia", "Greece", "Japan", "Korea")
(Wine, Pelmeni, *Fish) = countries 
print(Wine)
print(Pelmeni)
print(Fish)

brand = ("Google", "Zara", "Massimo", "HM", "Starbucks")
(IT, *Fashion, Coffee) = brand
print(IT)
print(Fashion)
print(Coffee)

countries_brand = countries + brand
print(countries_brand)

newtuple = brand * 2
print(newtuple)



