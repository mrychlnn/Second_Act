# PROG_01: Create a program that ask user to input 2 numbers. Print the bigger number.

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if num1 > num2:
    print (f"{num1:.2f} is the bigger number")
else:
    print (f"{num2:.2f} is the bigger number")