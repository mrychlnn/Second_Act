#PROG_06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

exponent = num1 ** num2

print (f"The answer for 1st number raised to the 2nd number is {exponent:.2f}") 