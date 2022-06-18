#!/usr/bin/env python3
"""Game that that uses the crayons library"""

#install the crayons package
#python3 -m pip install crayons
#import crayons package. Statement always goes on top before main code
import crayons

"""run time code. Always indent under function"""
print(crayons.red(f"Hello, Welcome to my Python game.\nCan you guess the number I'm thinking?. You have 10 tries", bold=True))

def status():
    
    count = 10

    while count > 0:
        #ask user to input a number
        user_input = int(input("Enter the number: "))
        if user_input == 23:
            print(crayons.green(f"YOU WIN", bold=True))
            print(crayons.yellow(f"The game has ended. Goodbye!", bold=True))
            break
        
        print(crayons.blue(f"Wrong answer. You have {count-1} attempts remaining....", bold=True))
        count = count - 1 
    else:
        print(crayons.yellow(f"Sorry you lost the game :(", bold=True))

def main():
    status()
main()




