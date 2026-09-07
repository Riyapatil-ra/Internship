''' Write a Python program to generate a multiplication table from 1 to 10.
* The program must use nested for loops.
* The output should clearly display each multiplication table separately.
* Additional requirement: Skip the multiplication table of 5 and stop generating tables after the table of 8.
'''
n=int(input("Enter the number to generate multiplication tables: "))
for i in range(1,n+1):
    if i==5:
        continue
    if i>8:
        break
    print(f"Multiplication Table of {i}:")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print()