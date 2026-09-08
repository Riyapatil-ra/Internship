'''                                             File Handling

* open() = Open a file
* "r" = Read a file
* "a" Write to a file
* "w"= Append to a file
* "x"= Create a file
* "r+"= Read and write to a file
* Close a file
* "t" = Text mode
* "b" = Binary mode
'''

# f=open("demo.txt") 
# ''' or '''
# f=open("demo.txt","rt") # default mode is "rt"
# print(f.read())
# f.close()
# with open("demo.txt") as f:
#     print(f.read())

# with open("demo.txt","rt") as f:
#     print(f.read(5))
#     print(f.readline())
#     print(f.readline())

# with open("demo.txt","rt") as f:
#     print(f.read())
#     for i in f:
#         print(i)

''' Write to a file
* "a" = Append to the end of the file
* "w" = Overwrite to a file
'''
# with open("demo.txt", "a") as f:
#   f.write("Now the file has more content!")
# #open and read the file after the appending:
# with open("demo.txt") as f:
#   print(f.read())

# with open("demo.txt", "w") as f:
#   f.write("Woops! I have deleted the content!")
# #open and read the file after the appending:
# with open("demo.txt") as f:
#   print(f.read())

# ''' Create a new file'''
# f=open("myfile.txt", "x")

''' Delete a file
* import os'''

# import os
# os.remove("demo.txt")

# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")

# os.rmdir("myfolder")

'''                                           Python OOP                                                  '''
''' Advantages of OOP: 
* Code reusability
* Code maintainability
* Code flexibility
* Code testability
'''
''' Classes and Objects
* Python is an object oriented programming language.
* A class defines what an object should look like, and 
an object is creadted based on that class.
'''
''' Create a Class and class object
* To create a class, use the keyword class:
'''
# class MyClass:
#   x = 5
#   y=78
# pi=MyClass()
# del pi
# print(pi.x,pi.y)

''' The pass Statement
* class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
'''
# class person:
#   pass

# class Person:
#    def __init__(self,name,age):
#        self.name=name
#        self.age=age
#    def greet(self):
#        print("Hello,my name is ",self.name)

# p1=Person("John",36)
# p1.greet()

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("Emil", 36)

# print(p1.name)
# print(p1.age)

# class Person:
#   def __init__(self, name, age=18):
#     self.name = name
#     self.age = age

# p1 = Person("Emil")
# p2 = Person("Tobias", 25)

# print(p1.name, p1.age)
# print(p2.name, p2.age)

# class Person:
#   def __init__(self, name, age, city, country):
#     self.name = name
#     self.age = age
#     self.city = city
#     self.country = country

# p1 = Person("Linus", 30, "Oslo", "Norway")

# print(p1.name)
# print(p1.age)
# print(p1.city)
# print(p1.country)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def greet(self):
#     print("Hello, my name is " + self.name)

# p1 = Person("Emil", 25)
# p1.greet()

# class Person:
#   def __init__(myobject, name, age):
#     myobject.name = name
#     myobject.age = age

#   def greet(abc):
#     print("Hello, my name is " + abc.name)

# p1 = Person("Emil", 36)
# p1.greet()

''' Accessing Properties with self'''
# class Car:
#   def __init__(self, brand, model, year):
#     self.brand = brand
#     self.model = model
#     self.year = year

#   def display_info(self):
#     print(f"{self.year} {self.brand} {self.model}")

# car1 = Car("Toyota", "Corolla", 2020)
# car1.display_info()

# class Person:
#   def __init__(self, name):
#     self.name = name

#   def greet(self):
#     return "Hello, " + self.name

#   def welcome(self):
#     message = self.greet()
#     print(message + "! Welcome to our website.")

# p1 = Person("Tobias")
# p1.welcome()

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("Tobias", 25)
# print(p1.age)
# p1.age = 26
# print(p1.age)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("Linus", 30)
# del p1.age
# print(p1.name)
# print(p1.age)  # This will raise an AttributeError since 'age' has been deleted

''' class property vs. object property
* Class properties are shared among all instances of the class, while object properties are unique to each
'''
# class Person:
#   species = "Human" # Class property

#   def __init__(self, name):
#     self.name = name # Instance property

# p1 = Person("Emil")
# p2 = Person("Tobias")

# print(p1.name)
# print(p2.name)
# print(p1.species)
# print(p2.species)

'''Modifying Class Properties'''
# class Person:
#   lastname = ""
#   def __init__(self, name):
#     self.name = name

# p1 = Person("Linus")
# p2 = Person("Emil")
# Person.lastname = "Refsnes"
# print(p1.lastname)
# print(p2.lastname)

''' Add new Properties'''
# class Person:
#   def __init__(self, name):
#     self.name = name

# p1 = Person("Tobias")
# p1.age = 25
# p1.city = "Oslo"
# print(p1.name)
# print(p1.age)
# print(p1.city)

''' Class Methods '''
# class Calculator:
#   def add(self, a, b):
#     return a + b

#   def multiply(self, a, b):
#     return a * b

# calc = Calculator()
# print(calc.add(5, 3))
# print(calc.multiply(4, 7))

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def celebrate_birthday(self):
#     self.age += 1
#     print(f"Happy birthday! You are now {self.age}")

# p1 = Person("Linus", 25)
# p1.celebrate_birthday()
# p1.celebrate_birthday()

''' __str__() Method
* The __str__() method is used to return a string representation of an object.
'''
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name} {self.age}"

# p1 = Person("Tobias", 36)
# print(p1)