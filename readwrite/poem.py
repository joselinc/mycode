#!/usr/bin/env python

def main():
    #open the text1.txt file in default read mode
    final_poem = open("text1.txt")
    #read the size of the poem 
    final_poem.read(size)
    #writes to the end of the poem the name of the author
    final_poem = write("Pablo Neruda <3")
    #prints the updated poem
    print(final_poem)
    #closes the file
    final_poem.close()

main()
