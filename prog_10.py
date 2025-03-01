#PROG_10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

print("The numbers starting from 0 to 100 w/o numbers end with zero are:")
for number in range(101):
    if number % 10 != 0:
        print(number)