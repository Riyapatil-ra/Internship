''' Python Iterators
* An iterator is an object that contains a countable number of values.
* An iterator is an object that can be iterated upon,
 meaning that you can traverse through all the values.
* Technically, in Python, an iterator is an object which implements the iterator protocol, 
which consist of the methods __iter__() and __next__()
'''

''' Iterator vs Iterable
* Lists, tuples, dictionaries, and sets are all iterable objects. 
* They are iterable containers which you can get an iterator from.
* All these objects have a 
iter() method which is used to get an iterator
'''
mytuple = ("apple", "banana", "cherry")
mystr="banana"
# myit = iter(mytuple)
# myit2=iter(mystr)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit2))
# print(next(myit2))

''' Looping Through an Iterator'''
# for x in mytuple:
#   print(x)

# for x in mystr:
#   print(x)

''' Create an Iterator
* The __iter__() method acts similar, you can do operations (initializing etc.), 
but must always return the iterator object itself.
* The __next__() method also allows you to do operations, and must return the next item in the sequence.
'''

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

''' StopIteration
* The example above would continue forever if you had enough next() statements,
* To prevent the iteration from going on forever, we can use the StopIteration statement.
'''
# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     if self.a <= 20:
#       x = self.a
#       self.a += 1
#       return x
#     else:
#       raise StopIteration

# myclass = MyNumbers()
# myiter = iter(myclass)

# for x in myiter:
#   print(x)

''' Python Modules'''

''' Create a Module
* Save the code you want in a file with the file extension .py
* syntax: module_name.py
* syntax: import module_name
* syntax: module_name.function_name
'''
# import mymodule
# mymodule.greeting("Jonathan")
# a=mymodule.person1["age"]
# print(a)

''' Naming Module'''
# import mymodule as mx
# a=mx.person1["age"]
# print(a)

''' Built-in Modules'''
# import platform
# x=platform.system()
# print(x)
# y=dir(platform)
# print(y)

''' Import From Module
* from module_name import function_name
* from module_name import function_name as fn
'''
# from mymodule import person1
# print(person1["age"])

''' Python Datetime'''
import datetime
# x = datetime.datetime.now()
# print(x)
# print(x.date())
# print(x.year)
# print(x.strftime("%A"))
# print(x.hour)
# print(x.second)
# print(x.day)

''' Creating Date Objects
* The datetime() class requires three parameters to 
create a date: year, month, day.
'''
# y=datetime.datetime(2020, 5, 17)
# print(y)


''' The strftime() Method
* The strftime() method allows you to format date objects into readable strings.
* The method takes one parameter, format, to specify the format of the returned string.
'''
# z=datetime.datetime(2018,6,1)
# print(z.strftime("%B"))

'''
Directive	Description	Example	
%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%C	Century	20	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%	
%G	ISO 8601 year	2018	
%u	ISO 8601 weekday (1-7)	1	
%V	ISO 8601 weeknumber (01-53)	01
'''

''' Python Math'''
# x=min(5,10,24)
# y=max(5,10,24)
# z=abs(-7.25)
# a=pow(2,3)
# print(f"Minimum value is: {x} and Maximum value is: {y}")
# print(f"Absolute value is: {z}")
# print(f"Power value is: {a}")

# import math
# print(math.sqrt(16))
# print(math.ceil(4.2)) # round upward
# print(math.floor(4.2)) # round downword
# print(math.pi)

''' Python JSON
* JSON is a syntax for storing and exchanging data.
'''
import json

''' Convert from JSON to Python'''
# Parse JSON
# x = '{"name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)
# print(y)

# ''' convert Python object to JSON '''
# z = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }
# a = json.dumps(z)
# print(a)

''' You can convert Python objects of the following types, 
into JSON strings:
* dict
* list
* tuple
* string
* int
* float
* True
* False
* None
'''
# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

'''
Python	JSON
dict	Object
list	Array
tuple	Array
str	    String
int	    Number
float	Number
True	true
False	false
None	null
'''

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# print(json.dumps(x))

''' Format the Result'''
# print(json.dumps(x, indent=4, separators=(". ", " = "), sort_keys=True))

''' Python RegEx
* A RegEx, or Regular Expression, is a sequence of characters 
that forms a search pattern.
* RegEx can be used to check if a string 
contains the specified search pattern
'''

# import re
# txt="The rain in Spain"
# # search the string to see if it starts with "The" and ends with "Spain":
# x=re.search("^The.*Spain$",txt)
# if x:
#     print("YES! We have a match!")
# else:
#     print("No match")

''' RegEx Functions
# **Function**   **Description**
# findall	        Returns a list containing all matches
# search	        Returns a Match object if there is a match anywhere in the string
# split	        Returns a list where the string has been split at each match
# sub	            Replaces one or many matches with a string
# '''

# ''' Metacharacters
# Character	Description	                               Example	
# []	        A set of characters	                       "[a-m]"	
# \	      Signals a special sequence 	               "\d"	
# .	      Any character (except newline character)	   "he..o"	
# ^	      Starts with	                                "^hello"	
# $	      Ends with	                                    "planet$"	
# *	      Zero or more occurrences	                    "he.*o"	
# +	      One or more occurrences	                    "he.+o"	
# ?	      Zero or one occurrences	                    "he.?o"	
# {}	      Exactly the specified number of occurrences	"he.{2}o"	
# |	      Either or	                                    "falls|stays"	
# ()	       and group
# '''

# ''' Flags
# Flag	        Shorthand	Description	
# re.ASCII	    re.A	    Returns only ASCII matches	
# re.DEBUG		            Returns debug information	
# re.DOTALL	    re.S	    Makes the . character match all characters (including newline character)	
# re.IGNORECASE	re.I	    Case-insensitive matching	
# re.MULTILINE	re.M	    Returns matches at the start/end of each line	
# re.NOFLAG		            Specifies that no flag is set for this pattern	
# re.UNICODE	    re.U	    Returns Unicode matches. This is default from Python 3. For Python 2: use this flag to return only Unicode matches	
# re.VERBOSE	    re.X	    Allows whitespaces and comments inside patterns. Makes the pattern more readable

# '''

# ''' Special Sequences
# Character	Description	                                                                                    Example	
# \A	        Returns a match if the specified characters are at the beginning of the string	                "\AThe"	
# \b	        Returns a match where the specified characters are at the beginning or at the end of a word     r"\bain",r"ain\b
# \B	        Returns a match where the specified characters are present, but NOT at the beginning 	        r"\Bain",r"ain\B"	
# \d	        Returns a match where the string contains digits (numbers from 0-9)	                            "\d"	
# \D	        Returns a match where the string DOES NOT contain digits	                                    "\D"	
# \s	        Returns a match where the string contains a white space character	                            "\s"	
# \S	        Returns a match where the string DOES NOT contain a white space character	                    "\S"	
# \w	        Returns a match where the string contains any word characters                               	"\w"	
# \W	        Returns a match where the string DOES NOT contain any word characters	                        "\W"	
# \Z	        Returns a match if the specified characters are at the end of the string	                    "Spain\Z"	
# ''' 
# ''' Sets
# [arn]	    Returns a match where one of the specified characters (a, r, or n) is present	
# [a-n]	    Returns a match for any lower case character, alphabetically between a and n	
# [^arn]	    Returns a match for any character EXCEPT a, r, and n	
# [0123]	    Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
# [0-9]	    Returns a match for any digit between 0 and 9	
# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
# [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
# [+]	        In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
# '''

''' The findall()'''
# import re

# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)

# y= re.findall("Portugal", txt)
# print(y)

''' The search() function'''
# txt = "The rain in Spain"
# x = re.search("\s", txt)
# print("The first white-space character is located in position:", x.start())
# y = re.search("Portugal", txt)
# print(y)

''' The split() function'''
# x = re.split("\s", txt)
# print(x)
# y = re.split("\s", txt, 1)
# print(y)

''' The sub() function'''
# z = re.sub("\s", "9", txt)
# print(z)
# x = re.sub("\s", "9", txt, 2)
# print(x)

# import re

# txt = "The rain in Spain"
# x = re.search("ai", txt)
# print(x)

''' Python PIP
* PIP is a package manager 
for Python packages, or modules if you like.
'''

''' Package
* A package contains all the files you need for a module.
'''
# import camelcase
# c = camelcase.CamelCase()
# txt = "hello world"
# print(c.hump(txt))

''' Python Try Except
* The try block lets you test a block of code for errors.
* The except block lets you handle the error.
* The else block lets you execute code when there is no error.
* The finally block lets you execute code, 
regardless of the result of the try- and except blocks.
'''
''' Exception Handling'''
# try:
#     print(x)
# except:
#     print("An exception occurred")

# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")

# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")

# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")

# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")

''' Raising Exceptions
* As a Python developer you can choose to throw an exception if a condition occurs.
'''
# x = -1
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")

# x = "hello"
# if not type(x) is int:
#   raise TypeError("Only integers are allowed")

# x=None
# print(type(x))
# if x is not None:
#     print("x is None")
# else:
#     print("x is not None")

# print(bool(None)) # False
# def myfunc():
#   x = 5
# x = myfunc()
# print(x)

# name = input("Enter your name: ")
# print("Hello, " + name)

# name = input("Enter your name:")
# print(f"Hello {name}")
# fav1 = input("What is your favorite animal:")
# fav2 = input("What is your favorite color:")
# fav3 = input("What is your favorite number:")
# print(f"Do you want a {fav2} {fav1} with {fav3} legs?")

# import math
# x = input("Enter a number:")

# #find the square root of the number:
# y = math.sqrt(float(x))

# print(f"The square root of {x} is {y}")

# y = True
# while y == True:
#   x = input("Enter a number:")
#   try:
#     x = float(x);
#     y = False
#   except:
#     print("Wrong input, please try again.")

# print("Thank you!")

''' Python Virtual Environment'''
# Creating=python -m venv myfirstproject
# Activate=myfirstproject\Scripts\activate
# Deactivate=myfirstproject\Scripts\deactivate
# delete= rmdir /s /q myfirstproject

''' File Handling

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

''' Python OOP'''
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
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} {self.age}"

p1 = Person("Tobias", 36)
print(p1)

