#!/usr/bin/env python3

#creates a list called list1
list1 = ["192.168.0.5", 500, "UP"]

#This line prints the first item from a list
print("The first item in the list is " + list1[0])

#This line prints the second item from the list
print("The first item in the list is " + str(list1[1]))

#This line prints the third line from the list
print("The first item in the list is " + list1[2])

#This line creates a new list
list2 = [500, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

#This line prints the IP address only from the above list
print("The IP addresses from the list are:", list2[3],"and", list2[4])
