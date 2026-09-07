''' Write a Python program that accepts two numbers from the user and performs division.
The program must properly handle:
   * Invalid/non-numeric input
   * Division by zero
   * Unexpected errors
The program should display an appropriate error message instead of terminating unexpectedly.
'''

try:
    a=float(input("Enter the first number: "))
    b=float(input("Enter the second number: "))
    divide=a/b
    print(f"Division of {a} by {b} is: {divide}")

except ValueError:
    print("Invalid input! Enter numeric values only.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

