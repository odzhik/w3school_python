mytuple = ("BMW", "Porsche", "Mercedes")
myiterator = iter(mytuple)

print(next(myiterator))
print(next(myiterator))
print(next(myiterator))

mystr = "Mercedes"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

for x in mytuple:
    print(x)
for x in mystr:
    print(x)


class MyNum:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
    
myclass = MyNum()
myiter = iter(myclass)

for x in myiter:
    print(x)

