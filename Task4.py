''' Write a Python program that accepts a string from the user and checks whether it is a palindrome'''
s=input("Enter a string:")
s=s.lower()
rev=""
for i in range(len(s)-1,-1,-1):
    rev+=s[i]

if s==rev:
    print("Palindrome")
else:
    print("Not a Palindrome")