#!/usr/bin/env python3

def main():
    #created the string hostname
    hostname = input("What's the value we set for hostname?\n")
    #test login with the if statement

    if hostname.lower() == "mtg":
        print("The hotsname was found to be mtg")
        print("hostname matches expected config")

    print("Existing the script")

main()
