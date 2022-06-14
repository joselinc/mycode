#!/usr/bin/env python3

def main():

    #create a new list
    a = ["cat", "bunny", "bird", "dog"]
    #print the list
    print(a)
    
    #convert that list into a string
    pets = " ".join(a)
    #print the string
    print(pets)

    pets = pets.title()
    #capitalize the string
    print(pets)

    b = pets.split()
    print(b)

main()
