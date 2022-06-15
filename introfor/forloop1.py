#!/usr/bin/env python

def main():

    #create a list of vendor
    vendors = ["cisco", "juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]
    #creates a second list of vendors
    approved_vendors = ["cisco", "juniper", "big_ip"]
    #loop across the list vendors
    for vendor in vendors:
        print("\nThe vendor is:", vendor, end="") #each time though the loop print value of x
        if vendor not in approved_vendors:
            print(" - NOT AN APPROVED VENDOR!", end="")
    print("\n The loop has ended.") #when the loop ends print this

main()
