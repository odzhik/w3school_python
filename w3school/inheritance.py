# parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    

    def printname(self):
        print(self.firstname, self.lastname)


# x = Person("Olzhas", "Zhakayev")
# x.printname()

# class Student(Person): # Student is a child class, Person is a Parent class
#     pass # when u dont want to change anything print pass

# x = Student("Alibi", "Sadykov")
# x.printname()

# class Student(Person):
#     def __init__(self, fname, lname):
#         # Person.__init__(self, fname, lname) # or
#         super().__init__(self, fname, lname) # super() automatically will call parent class

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x = Student("Yergen", "Kuantay", 2019)
print(x.graduationyear)
x.welcome()





