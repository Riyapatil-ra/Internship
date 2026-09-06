# Membership Operators
''' 
Membership operators are used to test if a 
sequence is presented in an object:
'''
# fruits=['Mango','Cherry','Apple','Banana','Oranges']
# print('Cherry' in fruits)
# print('e' in fruits)
# print('go' in fruits)
# print('Oranges' in fruits)

# s='beautiful'
# print('bea' in s)
# print('b' in s)
# print('ful' in s)
# print('B' in s)

# t=(1,2,'a','b')
# print(1 in t)
# print('a' in t)
# print('d' in t)

# print('d' not in t)

# Bitwise Operators
'''
Bitwise operators are used to compare binary numbers:
0=0000 1=0001 2=0010 3=0011 4=0100 5=0101 6=0110 7=0111 
8=1000 9=1001 A=1010 B=1011 C=1100 D=1101 E=1110 F=1111
'''

'''Bitwise AND (&) operator '''
# print(6 & 3) # 2
'''Bitwise OR (|) operator '''
# print(6 | 3)  # 7
'''Bitwise XOR (^) operator '''
# print(6 ^ 3) # 5
'''Bitwise NOT (~) operator  ~(n)=-(n+1)'''
# print(~3)  # -4
'''Bitwise Left Shift (<<) operator '''
# print(4 << 2) # 16
'''Bitwise Right Shift (>>) operator '''
# print(4 >> 2) # 1
# print(3 >> 2) # 0

# List
''' 
* List are used to store multiple items in a single variable.
* Lists are one of 4 built-in data types in python used to store 
collections of data, the other 3 are Tuple, Set, and Dictionary, all with
different qualities and usage.
* Lists are created using square brackets.
'''

# l=[12,5,13,78,54]
# print(*l)

''' List items are ORDERED,INDEXED, 
CHANGEABLE, and allow DUPLICATES values.'''

#  l=[22,5,13,78,54,9,22]
# print(*l)

''' List length'''
# print(len(l))

''' List Items- Data Types'''
# l1=['apple','banana','cherry']
# l2=[1,2,3,4]
# l3=[True,False,False]
# print(l1,type(l1))
# print(l2,type(l2))
# print(l3,type(l3))
# l4=['abc',34,True,40,'male']
# print(l4,type(l4))

# ''' The list() Constructor'''
# l5=list((1,2,3,4,5,6))
# print(l5,type(l5))

''' Python Collections (Arrays)
There are four collection data types in the Python programming language:

* List is a collection which is ORDERED and CHANGEABLE. 
Allows DUPLICATE members.
* Tuple is a collection which is ORDERED and UNCHANGEABLE. 
Allows DUPLICATE members.
* Set is a collection which is UNORDERED, UNCHANGEABLE, and UNINDEXED.
No DUPLICATE members.
* DICTIONARY is a collection which is ORDERED and CHANGEABLE. 
No DUPLICATE members
'''

''' Access List Items
List items are indexed:
'''

l1=['apple','banana','cherry','orange','kiwi','melon','mango']
# print(l1)
# print(l1[0])
# print(l1[-1])
# print(l1[2:6])
# print(l1[:4])
# print(l1[2:])
# print(l1[-4:-1])
# print(l1[::-1])

# if 'grape' in l1:
#     print("yes")
# else:
#     print("no")

''' Change Item Values'''
# l1[2]="lemon"
# print(l1)
# l1[3:6]=['Tomatos','Brinjal','Potatos']
# print(l1)
# l1[1:2]=['Watermelon','Pineapple']
# print(l1)
# l1[1:3]=['Water','Sun']
# print(l1)
# l1[1:3]=['Earth']
# print(l1)

''' Add list items
* append(value)	Adds an element at the end of the list
* insert(index,value)	Adds an element at the specified position
* extend(iterable)	Add the elements of a list (or any iterable), to the end of the current list
'''

# l1.append('Car') 
# print(l1)

# l1.insert(3,'blueberry')
# print(l1)

# l2=[1,2,3]
# l1.extend(l2)
# print(l1)
# l3=('a','b','c')
# l1.extend(l3)
# print(l1)

''' Remove Specified Items
* remove(value)	Removes the first item with the specified value
* pop(index)	Removes the item at the specified position
* del list[index]	Removes the item at the specified position
* clear()	Removes all the elements from the list
'''

# l2=[1,2,3,4,1,2]
# l2.remove(2)
# print(l2)

# l1.pop()
# print(l1)
# l1.pop(2)
# print(l1)

# del l1[2]
# print(l1)

# l2.clear()
# print(l2)

''' Loop Through a list'''
# for items in l1:
#     print(items)

''' Loop Through the index numbers'''
# for i in range(len(l1)):
#     print(l1[i])

''' Using a While Loop'''
# i=0
# while i<len(l1):
#     print(l1[i])
#     i+=1

''' Looping Using List Comprehension'''
# [print(i) for i in l1]

''' List Comprehension
List comprehension offers a shorter syntax 
when you want to create a new list based on the values of 
an existing list.
'''

# new=[]
# for i in l1:
#     if 'a' in i:
#         new.append(i)
# print(new)

# new=[i for i in l1 if 'a' in i]
# print(new)
# print([i for i in range(10)])
# print([i.upper() for i in l1])
# print(['hello' for i in l1])
# print([x if x!='banana' else 'orange' for x in l1])

''' Sort List
* sort() Sorts the list ascending by default'''
# l1.sort()
# print(l1)

# l1.sort(reverse=True)
# print(l1)

# def demo(n):
#     return abs(n-50)

# l2=[100,50,65,82,23]
# l2.sort(key=demo)
# print(l2)

# ''' Case Insensitive Sort'''
# l3=['z','m','a','A','M','J']
# l3.sort()
# print(l3)

# l3.sort(key=str.lower)
# print(l3)

# ''' Reverse Order'''
# l1.reverse()
# print(l1)

''' Copy a List'''
# l4=l1
# print(l4)
# l1.append('Grapes')
# print(l1)
# print(l4)
# print()
''' the above method makes the list if original list
changes then this list also changes'''

# l5=l1.copy()
# print(l5)
# l1.pop()
# print(l1)
# print(l5)

# l5=list(l1)
# print(l5)
# l1.pop()
# print(l1)
# print(l5)

# l5=l1[:]
# print(l5)
# l1.pop()
# print(l1)

# l5=l1[:]
# print(l5)
# l1.pop()
# print(l1)
# print(l5)

'''Join Two Lists'''

# l4=['a','b','c']
# l5=[1,2,3,4]
# l6=l4 + l5
# print(l6)

# for i in l5:
#     l4.append(i)
# print(l4)

# l4.extend(l5)
# print(l4)

# l6=[1,2,3,4,1,2,5,6,2,2,3]
# a=[i for i in l6 if l6.count(i)>1]
# print(a)

''' Tuple 
* Tuples are used to store multiple items in a single variable.

* Tuple is one of 4 built-in data types in Python used to store collections of data, 
the other 3 are List, Set, and Dictionary, all with different qualities and usage.

* A tuple is a collection which is ordered and unchangeable.

* Tuples are written with round brackets*.
'''

# t1=('apple','banana','cherry')
# print(t1)

# t2='apple','banana','cherry'
# print(t2)

# t3=('apple','banana','cherry','apple')
# print(t3)

''' Tuple length'''
# print(len(t1))

''' Tuple with one item'''
# t4=('apple',) # tuple
# print(type(t4))
# t4=('apple') # str
# print(type(t4))

''' Create an empty tuple'''
# t4=()
# print(type(t4))

''' Tuple Items - Data Types'''
# t5=('apple',10,True) # tuple with different data types
# print(t5)

''' The tuple() Constructor'''
# t6=tuple(('apple','banana','cherry')) # note the double round-brackets
# print(t6)

''' Access Tuple Items'''
# print(t1[0])
# print(t1[-1])
# print(t1[2:5])
# print(t1[:4])
# print(t1[2:])
# print(t1[::-1])

# for i in t1:
#     print(i)

# y=list(t1)
# y[1]='mango'
# t1=tuple(y)
# print(t1)

''' Add tuple to tuple'''
# t4=(1,)
# t1+=t4
# print(t1)

''' delete tuple'''
# del t2
# print(t2)

''' Unpacking a Tuple
we are also allowed to extract the values back into variables. 
This is called "unpacking":
'''
# (green, yellow, red)=t1
# print(green)
# print(yellow)
# print(red)

# t2=(1,2,3,4,5)
# (green, yellow, *red)=t2
# print(green)
# print(yellow)
# print(red)

''' Same as List for looping'''
''' for join use  '+' , use '*' for multiplying tuple '''

# print(t1 * 2)

''' Set 
* A set is a collection which is UNORDERED, 
UNCHANGEBLE, and UNINDEXED.
* Sets are used to store multiple 
items in a single variable.
'''
# s1={'apple','banana','cherry'}
# print(s1)
# print(type(s1),len(s1))

''' duplicate values are not allowed in sets'''
# s2={'apple','banana','cherry','apple'}
# print(s2)

# s2={'apple','banana','cherry',True,1,2}
# print(s2)    # {True, 2, 'cherry', 'banana', 'apple'}

# s2={'apple','banana','cherry',False,True,0}
# print(s2)

# s2=set(('apple','banana','cherry')) # note the double round-brackets
# print(s2)

''' Access Set Items'''

# for i in s1:
#     print(i)

# print('banana' in s1)
# print('grape' not in s1)

''' Add Set Items'''
# s1.add('orange')
# print(s1)

''' Add set to set'''
# s1.update({'grape','mango'})
# print(s1)

# s1.update(['kiwi','watermelon'])
# print(s1)

''' Remove Set Items'''
# s1.remove('banana') # will raise an error if the item does not exist
# print(s1)
# s1.remove('bottel') # throw error as it does not exist
# print(s1)

# s1.discard('banana') # will not raise an error if the item does not exist
# print(s1)
# s1.discard('bottel') # doesn't throw error even it not exist
# print(s1)

# x=s1.pop() # removes a random item from the set
# print(x)
# print(s1)

# s1.clear() # empties the set
# print(s1)

# del s1
# print(s1)

''' Join Sets'''

''' UNION()'''
s2={'a','b','c',1,2}
s3={1,2,3,4,'a','b'}
s4={'d','e'}
s5={'f','g'}
# print(s2.union(s3))
# print(s2 | s3) # only allow set with set
# print(s2.union(s3,s4,s5))

# ''' Update()'''
# s2.update(s3) # chages original set
# print(s2)


# ''' INTERSECTION()'''
# print(s2.intersection(s3))
# print(s2 & s3) # only allow set with set

# ''' INTERSECTION_UPDATE()'''
# s2.intersection_update(s3) # chages original set
# print(s2)

# ''' DIFFERENCE()'''
# print(s2.difference(s3))
# print(s2-s3) # only allow set with set

# ''' DIFFERENCE_UPDATE()'''
# s2.difference_update(s3) # chages original set
# print(s2)

# ''' SYMMETRIC_DIFFERENCE()'''
# print(s2.symmetric_difference(s3))
# print(s2 ^ s3) # only allow set with set

# ''' SYMMETRIC_DIFFERENCE_UPDATE()'''
# s2.symmetric_difference_update(s3) # chages original set
# print(s2)

''' FROZENSET'''
# A frozen set is a set that is immutable, meaning you cannot change its elements after it is created.

# x=frozenset({'apple','banana','cherry'})
# print(x)
# print(type(x))

''' Frozen Methods'''
''' 
* copy()
* difference()
* intersection()
* isdisjoint()
* issubset()
* issuperset()
* symmetric_difference()
* union()
'''

''' Dictionary
* A dictionary is a collection which is ORDERES, 
CHANGEBLE and does not allow DUPLICATES.
'''

d1={'brand':'Ford','model':'Mustang','year':1964}
# print(d1)

# ''' Dictionary ITEMS'''
# print(d1['model'])

# d2={'brand':'Ford','model':'Mustang','year':1964,'year':2020}
# print(d2)

# print(len(d1))
# d2={'brand':'Ford','model':'Mustang','year':1964,'colors':['red','white','blue']}
# print(d2)

# d2=dict(name='John',age=36,country='Norway')
# print(d2)

# ''' Access Dictionary Items'''
# print(d1.get('model'))
# ''' Access Dictionary Items using keys() method'''
# print(d1.keys())
# ''' Access Dictionary Items using values() method'''
# print(d1.values())
# ''' Access Dictionary Items using items() method'''
# print(d1.items())

# if 'model' in d1:
#     print("yes")

# ''' Change Values'''
# d1['year']=2020
# print(d1)

''' Update Dictionary'''
# d1.update({'year': 2021})
# print(d1)

''' Remove Dictionary Items'''
# d1.pop('model')
# print(d1)
# d1.popitem() # removes the last inserted item
# print(d1)
# del d1['model']
# print(d1)
# del d1
# print(d1) # throws error as d1 is deleted

# d1.clear()
# print(d1) # empties the dictionary

# ''' Loop Through a Dictionary'''
# for x in d1:
#     print(x)
''' Print values'''
# for x in d1:
#     print(d1[x])
# for x in d1.values():
#     print(x)
''' Print keys'''
# for x in d1.keys():
#     print(x)
# ''' Print both keys and values'''
# for x, y in d1.items():
#     print(x, y)

''' Copy a Dictionary'''
# d2=d1.copy()
# print(d2)

# d2=dict(d1)
# print(d2)

''' Nested Dictionaries'''
# myfamily={
#     "child1": {
# "name": "Emil",
# "year": 2004
# },
#     "child2": {
# "name": "Tobias",
# "year": 2007
# },
#     "child3": { 
# "name": "Linus",
# "year": 2011
# }
# }   
# print(myfamily)

# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }
# print(myfamily)

''' Access Items in Nested Dictionaries'''
# print(myfamily["child2"]["name"])

# ''' loop Through Nested Dictionaries'''
# for x, obj in myfamily.items():
#   print(x)

#   for y in obj:
#     print(y + ':', obj[y])

# ''' fromkeys(), '''

''' Python Match
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
'''

# day=9
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid day")

# day = 6
# match day:
#   case 1 | 2 | 3 | 4 | 5:
#     print("Today is not a weekday")
#   case 6 | 7:
#     print("I love weekends!")

# month = 5
# day = 4
# match day:
#   case 1 | 2 | 3 | 4 | 5 if month == 4:
#     print("A weekday in April")
#   case 1 | 2 | 3 | 4 | 5 if month == 5:
#     print("A weekday in May")
#   case _:
#     print("No match")

''' Calling a Function'''
# def demo():
#     print("Hello from a function")

# demo()

# ''' Function Uses'''
# def demo(fah):
#     return (fah-32)* 5 / 9

# print(demo(77))
# print(demo(95))
# print(demo(50))

''' Function return Values'''
# def greet():
#     return 'Good Morning'
# mes=greet()
# print(mes)
# print(greet())

# def demo():
#     pass

''' Arguments
Arguments are specified after the function name, 
inside the parentheses. You can add as many 
arguments as you want,just separate them with a comma.
'''
def demo(name): # function(parameter)
    print(name+" is a good boy")
demo("Rohit") # function(argument)
demo('Ram')
demo('Shyam')
