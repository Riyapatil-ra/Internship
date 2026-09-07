''' Write a Python program that accepts a positive integer N from the user and processes numbers from 1 to N.
The program must demonstrate the meaningful use of:
for loop
while loop
break
continue
pass
The program should use appropriate conditions to perform different operations on the numbers.
'''
while True:
    n=int(input("Enter a number (enter 0 to exit) : "))
    if n==0:
        break
    if n<0:
        print("Negative Number")
        continue
    for i in range(1,n+1):
        if i==1:
            pass
        if i%2==0:
            print(f"{i} is Even")
        else:
            print(f"{i} is Odd")