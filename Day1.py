import sys
# print("Hello, World!")
print(sys.version)
if 2>1:
    print("2 is greter than 1")
    print("Nothing")

x=9
y="Be ready to learn"

print("Good Morning")
print("Leaarn to live")

print("Hello"); print("Morning"); print("Mam");
# print("Hello") print("Morning") print("Mam") it show error
print('hello')
print("Hello ",end="")
print("Sneha")
print(4)
print(2+3)
print(230000)

print("I am",21,'years old')

"""
This is a comment
written in
more than just one line
"""
print("Creation")

x=5
y="Hons"
print(x)
print(y)

x=4
x="Amy"
print(x)

x=str(3)
y=int(3)
z=float(3)
print(type(x),x)
print(type(y),y)
print(type(z),z)

# invalid variables name
# 2myavr="john"
# my-var="john"

# Camel case
myVarName="John"

# pascal case
MyVarName="John"

# snake case
my_var_name="John"

x,y,z="Orange","Banana","Cherry"
print(x)
print(y)
print(z)    

a=b=c="Orange"
print(a)
print(b)
print(c)

fruits=["mango","apple",'cherry']
x,y,z=fruits
print(x)
print(y)
print(z)

x="Python "
y="is "
z="fun"
print(x,y,z)
print(x+y+z)

x=9
y="Strive"
print(x+y)
print(x,y)

x="awesome"
def myfunc():
    x="fantastic"
    print("Python is " +x)
myfunc()
print("Python is " +x)

x="awesome"
def myfunc():
    global x
    x="fantastic"

myfunc()
print("Python is " +x)

''' Python has the following data types built-in by default, in these categories:

Text Type:	    str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	    set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	    NoneType
'''
x="Hello"
print(type(x)) # str
x=20
print(type(x)) # int
x=21.6
print(type(x)) # float
x=1j
print(type(x))# complex
x=['apple','mango','cherry']
print(type(x))# list
x=("apple",'mango','cherry')
print(type(x)) # tuple
x=range(6)
print(type(x)) # range
x={"name":"xyz","age":40}
print(type(x)) # dict
x={"apple","cherry","mango"}
print(type(x)) # set
x=frozenset({"apple","cherry","mango"})
print(type(x)) # frozenset
x=True
print(type(x)) # bool
x=b"Hello"
print(type(x)) # bytes
x=bytearray(5)
print(type(x)) # bytearray
x=memoryview(bytes(5))
print(type(x)) # memortview
x=None
print(type(x)) # NoneType

x=str(6)
print(type(x),x) # <class 'str'> 6
x=int(6)
print(type(x),x) # <class 'int'> 6
x=float(6)
print(type(x),x) # <class 'float'> 6.0
x=complex(9+1j)
print(type(x),x) # <class 'complex'> (9+1j)
x=list(("apple","banana","cherry"))
print(type(x),x) # <class 'list'> ['apple', 'banana', 'cherry']
x=tuple(("apple","banana","cherry"))
print(type(x),x) # <class 'tuple'> ('apple', 'banana', 'cherry')
x=range(6)
print(type(x),x) # <class 'range'> range(0, 6)
x=dict(name="Abhay",age=12)
print(type(x),x) # <class 'dict'> {'name': 'Abhay', 'age': 12}
x=set({1,2,3})
print(type(x),x) # <class 'set'> {1, 2, 3}
x=frozenset({1,2,3,4})
print(type(x),x) # <class 'frozenset'> frozenset({1, 2, 3, 4})
x=bool(6)
print(type(x),x) # <class 'bool'> True
x=bytes(6)
print(type(x),x) # <class 'bytes'> b'\x00\x00\x00\x00\x00\x00'
x=bytearray(6)
print(type(x),x) # <class 'bytearray'> bytearray(b'\x00\x00\x00\x00\x00\x00')
x=memoryview(bytes(6))
print(type(x),x) # <class 'memoryview'> <memory at 0x000002A16399CD00>

# int
x=5
y=35656222554887711
z=-3255522
print(type(x),x) 
print(type(y),y) 
print(type(z),z)

# float
x = 35e3
y = 12E4
z = -87.7e100
print(type(x),x)
print(type(y),y)
print(type(z),z)

# complex
x=3+5j
y=5j
z=-5j
print(type(x),x)
print(type(y),y)
print(type(z),z)

# Type conversion
x=1
y=7.8
z=7j
print(float(x))
print(int(y))
print(complex(x))

# random numbers
import random
print(random.randrange(1,10))

# type casting
a=int(1)
print(a)
a=int(2.8)
print(a)
a=int("3")
print(a)

b=float(1)
print(b)
b=float(2.8)
print(b)
b=float("3")
print(b)

c=str("s2")
print(c)
c=str(3)
print(c)
c=str(9.6)
print(c)

# string
print("It's alright")
print('Simple Meal')
print("He is called 'Leo'")
print('He is called "Leo"')

a="Hello"
print(a)

a="""Today's topic is Photosyntnesis .
we will learn about it in detail."""
b='''Today's topic is Photosyntnesis .
we will learn about it in detail.'''
print(a)
print(b)

a=" Good Morning  "
print(a[1])

for i in a:
    print(i)

print(len(a))
print("orn" in a)
print("arm" in a)

if "orn" in a:
    print("Yes, 'orm' is present in a")

if "arm" not in a:
    print("No, 'arm' is not present in a")

# slicing
print(a[3:7])
print(a[:6])
print(a[3:])
print(a[-7:-3])

# Modify strings

print(a.upper())
print(a.lower())
print(a.strip()) # remove whitespace from beg or end
print(a.replace("Morning","Evening"))
b="a,b,c,d,e"
print(b.split(",")) # splt string into substring

# string concatenation
a="Red"
b="Green"
print(a + b)
print(a + " " +b)

age=32
txt="My name is Suraj, I am " + age
print(txt)

# F-Strings
age=32
txt=f"My name is Suraj, I am {age} "
print(txt)

# placeholders and modifiers
''' AA placeholder can contain variables,operations,functions,and modifiers to format the value.'''
price=65
txt=f"The price is {price} dollars"
print(txt)
# '''A placeholder can include a modifier to format the value.
# A modifier is included by adding a colon : followed by a
# legal formatting type, like .2f which means 
# fixed point number with 2 decimals:'''
print(f"The price is {price:.2f} dollars")

# '''A placeholder can contain Pythom code, like math operations '''
print(f"The price is {20 * 40} dollars")

# # Escape characters
# print("We are the so-called "Vikings" from the north.")
print("We are the so-called \"Vikings\" from the north.")

print("It\'s alright.") # \'= single quote
print("It is \\ alright") # \\= backspace
print("Mango\nCherry") # \n = New Line
print("Good\rMorning") # \r = Carriage Return
print("Be\tReady") # \t = Tab
print("Be\bReady") # \b = Backspace
print("Be\fReady") # \f=form feed
print("\110\145\154") # \ooo=Octal value
print("\x48\x65") # ]xhh Hex value

# String methods
b="BE READY TO LEARN,BE READY TO GROW"
a="be ready to learn,be ready to grow"
c="ß"
d="123abcd"
e='2.1,2.4'
print(a.capitalize())
print(b.casefold())
print(c.casefold())
print(c.lower())
print(c.center(20))
print(a.count("e"))
print(a.encode())
print(a.endswith("grow"))
print(a.expandtabs())
print(a.find("work"))
txt="For only {price:.2f} dollars"
print(txt.format(price=50))
print(a.index("to"))
print(d.isalnum())
print(d.isalpha())
print(d.isascii())
print(e.isdecimal())
print(e.isdigit())
print(d.isidentifier())
print(b.islower())
print(e.isnumeric())
print(a.isprintable())
print(a.isspace())
print(a.istitle())
print(b.upper())

l=['a','b','c','d']
print('*'.join(l))

t='apple'
x=t.ljust(20)
print(x,"is my favourite fruits")

print(" bac  kal".lstrip())

txt="I like bananas"
mytable=str.maketrans("a",'g')
print(mytable)
print(txt.translate(mytable))

print(txt.partition("like"))

print(txt.replace("a","g"))
print(txt.rfind("v"))
# print(txt.rindex("v"))

x = txt.rjust(20)
print(x, "is my favorite fruit.")

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("apples")
print(x)

print("a,b,c".rsplit(","))
print("abcd df    ".rstrip())
print(txt.startswith("J"))
print("   b   ".strip())
print(a.swapcase())
print(a.title())
print(a.upper())
print("90".zfill(10))

# boolean operators
print(23>9)
print(23<10)
print(2==9)

print(bool("hello"))
print(bool(15))
print(bool(0))
print(bool([]))
print(bool(""))
print(bool(None))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

x=300
print(isinstance(x,int))

# ternary operator
num = 6
x = "WEEKEND!" if num > 5 else "Workday"
print(x)

num = 6
x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"
print(x)

# Identity operators
'''
Identity operators are used to compare the objects, not if they are equal, 
but if they are actually the same object, with the same memory location:
'''
a=["apple","mango","cherry"]
b=["apple","mango","cherry"]
x=10
y=10
c='a'
d='a'
e='abc'
f='abc'
j=(1,2,3)
k=(1,2,3)
r=[1,2,3]
s=[1,2,3]
t={1,2,3}
u={1,2,3}

print(f"Set: {t} {u}\n")
print(id(t))
print(id(u))
print(t is u)
print(f"\nList of nums: {r} {s}\n")
print(id(r))
print(id(s))
print(r is s)
print(f"\nTuple: {j} {k}\n")
print(id(j))
print(id(k))
print(j is k)
print(f"\nmulti char: {e} {f}\n")
print(id(e))
print(id(f))
print(e is f)
print(f"\nsingle char: {c} {d}\n")
print(id(c))
print(id(d))
print(c is d)
print(f"\nint: {x} {y}\n")
print(id(x))
print(id(y))
print(x is y)
print(f"\nList of words: {a} {b}\n")
print(id(a))
print(id(b))
print(a is b)

num1=[1,2,3]
num2=[1,2,3]
print(num1 is num2)
print(num1 is not num2)