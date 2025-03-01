#PROG_02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if num1 > num2:
    print (f"{num1:.2f} is the bigger number")
elif num2 > num1:
    print (f"{num2:.2f} is the bigger number")
else:
    print ("Both numbers are equal.")