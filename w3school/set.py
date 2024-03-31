# Unordered, unchanchable, unindexed

set1 = {"Italy", "Spain", "USA"}
print(type(set1))

# cant be duplicated values
countries = {"Italy", "Italy", "USA", "Spain"}
print(countries) # Italy, USA, Spain

newset = {"Tuple", "Dict", 1, True, False, 0, 2} # True and 1 same values, False and 0 same
print(newset)
print(len(newset))

thisset = set(("apple", "banana", "cherry"))
print(thisset)

for x in thisset:
    print(x)

thisset.add("Kiwi")
print(thisset)

thisset.update(countries)
print(thisset)
thisset.remove("Kiwi")
print(thisset)
thisset.discard("mango")
print(thisset) #If the item to remove does not exist, discard() will NOT raise an error.

x = thisset.pop() # remove a random item
print(x)
print(thisset)

thisset.clear() # clear all items in set
print(thisset)

# del thisset
# print(thisset) # completely delete set 

Company = {"HP", "Lenovo", "Apple"}
Banks = {"Kaspi", "RBK", "TInkoff"}

corp = Company.union(Banks)
print(corp)

# union and | are same

set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = set1 | set2
print(set3)

name = {"Nurdaulet"}
Surname = {"Syzdykov"}
Phone = {777}
Address = {"KRG"}
Info = name.union(Surname, Phone, Address) # or name | Surname | Address | Phone
print(Info)

x = {"VK", "Yandex", "Kaspi"}
y = {"Kaspi", "Halyk", "BCK"}

z = x.intersection(y) # & is intersection
print(z)
a = x.difference(y) # - is diff
print(a)
b = x.symmetric_difference(y) # ^ is symm difference
print(b)




