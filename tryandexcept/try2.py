#!/usr/bin/env python3
"""Review of try and except logic | Alta3 Research"""

def main():
    # Start with an infinite loop
    while True:
        try:
            #print("Enter a file name: ")
            #name = input()
            with open("farms.yaml", "w") as newfile:
                newfile.write("- name: E Farm\n  - agriculture:\n  - cows\n - tomatoes\n  - mangoes")
            break
        except:
            print("Error with that file! Try again...")

main()
