#!/usr/bin/env python3

print("Welcome to my calculator")
print("Select the number to perform an arithmetic operation:")
print("1 - Addition")
print("2 - Substraction")
print("3 - Multiplication")
print("4 - Division")

def main():
    
    option = input("Select a number: ")

    if option == "1":
        number1 = int(input("Please input the first number: "))
        number2 = int(input("Please input the second number: "))
        addition = number1 + number2
        print("The sum is:", addition)

    if option == "2":
        number1 = int(input("Please input the first number: "))
        number2 = int(input("Please input the second number: "))
        substraction = number1 - number2
        print("The substraction is:", substraction)

    if option == "3":
        number1 = int(input("Please input the first number: "))
        number2 = int(input("Please input the second number: "))
        multiplication = number1 * number2
        print("The multiplication is:", multiplication)

    if option == "4":
        number1 = int(input("Please input the first number: "))
        number2 = int(input("Please input the second number: "))
        division = number1 / number2
        print("The division is:", division)
main()
    

