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
#   lastname = "Kale" # Class property
#   def __init__(self, name):
#     self.name = name

# p1 = Person("Linus")
# p2 = Person("Emil")
# Person.lastname = "Refsnes" # Modifying class property
# print(p1.lastname)
# print(p2.lastname)

''' Add new Properties'''
# class Person:
#   def __init__(self, name):
#     self.name = name

# p1 = Person("Tobias")
# p1.age = 27
# p1.city = "Nagpur"
# print(p1.name)
# print(p1.age)
# print(p1.city)

''' Class Methods '''

''' Methods with Parametes'''
# class Calculator:
#   def add(self, a, b):
#     return a + b
#   def multiply(self, a, b):
#     return a * b

# calc = Calculator()
# print(calc.add(5, 3))
# print(calc.multiply(4, 7))

''' Methods Accessing Properties'''
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def get_info(self):
#     return f"{self.name} is {self.age} years old"

# p1 = Person("Tobias", 28)
# print(p1.get_info())

'''Methods Modifying Properties'''
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
* __str__() method is called When the class object is represented as a string, there is a method 
that controls what should be returned,
'''

# without __str__() method
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("Emil", 36)
# print(p1)

# with __str__() method
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name} {self.age}"

# p1 = Person("Tobias", 36)
# print(p1)

''' Multiple Methods
* A class can have multiple methods that works together
'''
# class Playlist:
#     def __init__(self,name):
#         self.name=name
#         self.songs=[]

#     def add(self,song):
#         self.songs.append(song)
#         print(f"Added: {song}")

#     def remove_song(self,song):
#         self.songs.remove(song)
#         print(f"Removed: {song}")

#     def show_song(self):
#         print(f"Playlist: {self.name}")
#         for song in self.songs:
#             print(f" - {song}")

# play=Playlist("Best Times")
# play.add("Sahiba")
# play.add("Tera Yaar Hoon Main")
# play.add("Sooraj Dooba Hain")
# play.add("Tere Mere")
# play.show_song()
# play.remove_song("Tera Yaar Hoon Main")
# play.remove_song("Tere Mere")
# play.show_song()

''' Delete Methods
* You can delete methods from a class using the del statement.
'''

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def greet(self):
#     print("Hello, my name is " + self.name)

#   def farewell(self):
#     print("Goodbye from " + self.name)

# p1= Person("Emil", 36)
# del p1.greet
# p1.farewell()
# p1.greet()  # This will raise an AttributeError since 'greet' method has been deleted

'''                                            Class Inheritance                                     
* Inheritance allows us to define a class that inherits all the methods and properties from another class.
* Parent class is the class being inherited from, also called base class.
* Child class is the class that inherits from another class, also called derived class.
'''
''' Create a Parent Class '''
# class Person:
#     def __init__(self,fname,lname):
#         self.first=fname
#         self.last=lname

#     def print(self):
#        print(self.first,self.last)

# p1=Person("Payal",'Mukind')
# p1.print()

''' Create a Child Class
* To create a class that inherits the functionality from another class, send the parent class as a
'''
# class Studnet(Person):
#     def demo(self):
#         print("This is a child class")
#         print(f"{Person.__name__} is the parent class of {Studnet.__name__}")
# x=Studnet("Mike","Olsen")
# print(x.first,x.last)
# x.print()
# x.demo()

''' Add the __init__() Function
* When you add the __init__() function, the child class will no longer 
inherit the parent's __init__() function.
* Note: The child's __init__() function overrides the 
inheritance of the parent's __init__() function.
* To keep the inheritance of the parent's __init__() function, add a 
call to the parent's __init__() function
* parent class_init__() function can be called using the super() function
'''

# class Student(Person):
#     def __init__(self,fname,lname):
#         Person.__init__(self,fname,lname)

''' Use the super() Function'''
# class Student(Person):
#     def __init__(self,fname,lname):
#         super().__init__(fname,lname)

''' Add Propertites'''
# class Student(Person):
#     def __init__(self,fname,lname):
#         super().__init__(fname,lname)
#         self.grad_year=2027
#         self.student_id="S001"

# x=Student("Mike","Olsen")
# print(x.first,x.last,x.grad_year,x.student_id)

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

# x = Student("Mike", "Olsen", 2019)
# print(x.graduationyear)

''' Add Methods'''
# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print("Welcome", self.first, self.last, "to the class of", self.graduationyear)

# s=Student("Mike", "Olsen", 2019)
# s.welcome()
# s.print()

'''                                             Python Polymorphism
* Polymorphism allows us to define methods in the child class with the same name as defined in their parent class.
* In inheritance, the child class inherits the methods from the parent class. 
However, it is possible to modify a method in a child class that it has inherited from the parent class. 
This is particularly useful in cases where the method inherited from the parent class does not quite fit the child class.
'''

'''Function Polymorphism'''
# x='language'
# y=('python','java','c++')
# z={'name':'payal','age':22}
# print(len(x),len(y),len(z))

'''Class Polymorphism'''
# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model

#     def move(self):
#         print("Drive!")

# class Boat:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model

#     def move(self):
#         print("Sail!")

# class Plane:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model

#     def move(self):
#         print("Fly!")

# car1=Car("Ford","Mustang")
# boat1=Boat("Yamaha","242X")
# plane1=Plane("Boeing","747")
# for vehicle in (car1,boat1,plane1):
#     vehicle.move()
# boat1.move()
# plane1.move()
# car1.move()

''' Inheritance Class Polymorphism'''
# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Move!")

# class Car(Vehicle):
#   pass

# class Boat(Vehicle):
#   def move(self):
#     print("Sail!")

# class Plane(Vehicle):
#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object

# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   x.move()

'''                                             Pyhton Encapsulation
* Encapsulation is the process of preventing direct access to the internal state of an object.
* It is achieved by using private attributes and methods.
* In Python, we use a single underscore (_) to indicate a private attribute or method.
* In Python, we use a double underscore (__) to indicate a strongly private attribute or method.
* The main purpose of encapsulation is to protect the data from being modified by external code.
* It also helps in organizing the code and making it more maintainable.     
'''

'''Private Properties'''
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age # Private property
# p1=Person("Tobias",25)
# print(p1.name)
# print(p1.__age) # This will raise an AttributeError since '__age' is a private property

''' Get Private Property value'''
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age # Private property

#     def get_age(self):
#         return self.__age
# p1=Person("Tobias",25)
# print(p1.name)
# print(p1.get_age())

''' Set Private Property value'''
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age # Private property

#     def get_age(self):
#         return self.__age

#     def set_age(self,age):
#         if age >= 0:    
#             self.__age=age
#         else:
#             print("Age cannot be negative")

# p1=Person("Tobias",25)
# print(p1.get_age())
# p1.set_age(30)
# print(p1.get_age())

''' Why Use Encapsulation?
* Data Protection: Prevents accidental modification of data
* Validation: You can validate data before setting it
* Flexibility: Internal implementation can change without affecting external code
* Control: You have full control over how data is accessed and modified
'''

# class Student:
#     def __init__(self,name):
#         self.name=name
#         self.__grade=0 # Private property

#     def set_grade(self,grade):
#         if 0 <= grade <= 100:
#             self.__grade=grade
#         else:
#             print("Grade must be between 0 and 100")

#     def get_grade(self):
#         return self.__grade

#     def get_status(self):
#         if self.__grade >= 60:
#             return "Passed"
#         else:
#             return "Failed"

# student=Student("Alice")
# student.set_grade(85)
# print(student.get_grade())
# print(student.get_status())

''' Protected Properties '''
# class Person:
#     def __init__(self, name, salary):
#         self.name = name
#         self._salary = salary  # Protected property

# p1=Person("Linus",300000)
# print(p1.name)
# print(p1._salary)  # This is accessible but should be treated as protected

''' Private Methods '''
# class Calculator:
#   def __init__(self):
#     self.result = 0

#   def __validate(self, num):
#     if not isinstance(num, (int, float)):
#       return False
#     return True

#   def add(self, num):
#     if self.__validate(num):
#       self.result += num
#     else:
#       print("Invalid number")

# calc = Calculator()
# calc.add(10)
# calc.add(5)
# print(calc.result)
# #calc.__validate(5) # This would cause an error

''' Name Mangling'''
# class Demo:
#   def __init__(self, name, age):
#     self.name = name
#     self.__age = age

# p1 = Demo("Emil", 30)

# # This is how Python mangles the name:
# print(p1._Demo__age) # Not recommended!

''' Python Inner Classes'''
# class Outer:
#     def __init__(self):
#         self.name="Outer Class"
#     class Inner:
#         def __init__(self):
#             self.name="Inner Class"
#         def display(self):
#             print("This is the inner class method")

# outer=Outer()
# print(outer.name)

''' Accessing inner class from outer class'''
# inner=outer.Inner()
# print(inner.name)
# inner.display()

''' Accessing outer class from inner class'''
# class Outer:
#   def __init__(self):
#     self.name = "Emil"

#   class Inner:
#     def __init__(self, outer):
#       self.outer = outer

#     def display(self):
#       print(f"Outer class name: {self.outer.name}")

# outer = Outer()
# inner = outer.Inner(outer)
# inner.display()

# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#     self.engine = self.Engine()

#   class Engine:
#     def __init__(self):
#       self.status = "Off"

#     def start(self):
#       self.status = "Running"
#       print("Engine started")

#     def stop(self):
#       self.status = "Off"
#       print("Engine stopped")

#   def drive(self):
#     if self.engine.status == "Running":
#       print(f"Driving the {self.brand} {self.model}")
#     else:
#       print("Start the engine first!")

# car = Car("Toyota", "Corolla")
# car.drive()
# car.engine.start()
# car.drive()

''' Multiple Inner Classes'''
# class Computer:
#   def __init__(self):
#     self.cpu = self.CPU()
#     self.ram = self.RAM()

#   class CPU:
#     def process(self):
#       print("Processing data...")

#   class RAM:
#     def store(self):
#       print("Storing data...")

# computer = Computer()
# computer.cpu.process()
# computer.ram.store()