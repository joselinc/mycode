#!/usr/bin/env python3
""" Conditionals - Life of Brian guessing game using a while True loop."""

def main():
    #sets a counter to 0
    round = 0

    while True:
        #counter starts increasing by 1
        round = round + 1
        #tells user to finish the movie
        print("Finish the movie title, 'Monty Python\'s The Life of _______'")
        #ask user to input their response
        answer = input("Your gues ---> ")
        #if the anser was correct it will print a correct message
        if answer == "Brian":
            print("Correct!")
            break  # break statement escapes the while loop
        #if the user exceed the 3 inputs, the game will be over
        elif round == 3:
            print("Sorry, the answer was Brian.")
            break   # break statement escapes the while loop
        else:
            print("Sorry, try again.")

main() 
