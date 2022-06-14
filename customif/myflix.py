#!/usr/bin/env python3

#if, elif, else - A simple program using conditionals to make a decision.

#define main function
#def main():
print("Welcome to our Movie Library")
print("-------------------------------\n")

def main():
    #will ask user to pick a number from 1 to 4
    number = input("Pick a number from 1 to 4 to show the movies we have in store\n")

    # if number is 1
    if number == "1":
        print("Harry Potter\n'Harry Potter is a series of seven fantasy novels written by British author J. K. Rowling. The novels chronicle the lives of a young wizard, Harry Potter, and his friends Hermione Granger and Ron Weasley, all of whom are students at Hogwarts School of Witchcraft and Wizardry. The main story arc concerns Harry's struggle against Lord Voldemort, a dark wizard who intends to become immortal, overthrow the wizard governing body known as the Ministry of Magic and subjugate all wizards and Muggles' - Wikipedia")

    #if number is 2
    elif number == "2":
        print("Hobbit & Lord of the Rings\n'The Lord of the Rings is the saga of a group of sometimes reluctant heroes who set forth to save their world from consummate evil. Its many worlds and creatures were drawn from Tolkien's extensive knowledge of philology and folklore.' - Wikipedia")
    
    #if number is 3
    elif number == "3":
        print("Chronicles of Narnia\n'The Chronicles of Narnia is a series of seven fantasy novels by British author C. S. Lewis. Illustrated by Pauline Baynes and originally published between 1950 and 1956, The Chronicles of Narnia has been adapted for radio, television, the stage, film and video games. The series is set in the fictional realm of Narnia, a fantasy world of magic, mythical beasts and talking animals. It narrates the adventures of various children who play central roles in the unfolding history of the Narnian world.' - Wikipedia")

    #if number is 4
    elif number == "4":
        print("Indiana Jones\n'Epic tale in which an intrepid archaeologist tries to beat a band of Nazis to a unique religious relic which is central to their plans for world domination. Battling against a snake phobia and a vengeful ex-girlfriend, Indiana Jones is in constant peril, making hair's-breadth escapes at every turn in this celebration of the innocent adventure movies of an earlier era.' - Wikipedia")
    
    #if it's a different number
    else:
        print("You selected the wrong number. Please try again")

#call the main function 
main()
