list = ["BMW", "Mercedes", "Audi"] # BMW - 0, Mercedes - 1, Audi - 2
print(list)

# List items are ordered, changeable, and allow duplicate values.

# List items are indexed, the first item has index [0], the second item has index [1] etc.

# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:

# Example
# Lists allow duplicate values:
car_list = ["BMW", "Mercedes", "Audi", 'BMW', "Audi"]
print(car_list)
print(len(car_list))

car_list = ["BMW", "Audi", "Mercedes", "VW", "Bugatti"]# BMW - 0, Audi - 1, Mercedes - 2
model_list = ["5 series", "A6", "C class"]
price_list = [30000, 27000, 35000]
stock_list = [True, False, False]
full_info_list = ["BMW", "5 series", 30000, True]
print(price_list)
print(stock_list)
print(full_info_list)
print(type(full_info_list))
print(car_list[1]) # Audi
print(car_list[-1]) # -1 is last, -2 предпоследний
print(car_list[0:6])
print(car_list[:6])
print(car_list[0:])
print(car_list[-5:-1])# -1 (last one) not included
if "BMW" in car_list:
    print("Yes")
if "Volvo" in car_list:
    print("Yes")
else:
    print("No")

# Change Item Value
# To change the value of a specific item, refer to the index number:

car_list[1] = "Lamborgini"
print(car_list[1])

car_list[0:5] = ["Ferrari", "Alfa Romeo", "Lamborgini", "Fiat", "Maserati"]
print(car_list[0:5])

car_list[3:4] = ["Pagani", "Koenigsegg"]
print(car_list)
car_list[1:6] = ["Ferrari"]
print(car_list)

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

# The insert() method inserts an item at the specified index:
car_list = ["Ferrari", "Lamborgini"]
car_list.insert(3, "Toyota") 
print(car_list) # new item in list 
# To add an item to the end of the list, use the append() method:
car_list.append("Lexus") # adds to the end
print(car_list)

car_list.extend(model_list) # combine 2 lists to 1
print(car_list)
car_list.remove("Toyota")
print(car_list)

american_brands = ["Chevy", "Ford", "GMC", "RAM", "Dodge", "Ford"] # there are 2 Ford
american_brands.remove("Ford") # remove only first Ford, second stay in the list
print(american_brands) 

# The pop() method removes the specified index.
american_brands.pop(3) # remove item by index
print(american_brands)

# If you do not specify the index, the pop() method removes the last item.
american_brands.pop()
print(american_brands)


american_brands = ["Chevy", "Ford", "GMC", "RAM", "Dodge", "Ford"]
del american_brands[0]
print(american_brands)

# The del keyword can also delete the list completely.
del american_brands

# Clear the List
# The clear() method empties the list.

# The list still remains, but it has no content.
american_brands = ["Chevy", "Ford", "GMC", "RAM", "Dodge", "Ford"]
american_brands.clear()
print(american_brands)

thislist = ["apple", "banana", "cherry"] 
for x in thislist: # loop all items
  print(x)

