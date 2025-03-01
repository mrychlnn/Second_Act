#PROG_5: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

quotient = num1 / num2

print (f"The quotient of the two numbers is {quotient:.2f}") 