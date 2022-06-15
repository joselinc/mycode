#!/usr/bin/env python3

def main():
    #open file in read mode
    dnsfile = open("dns_servers.txt", "r")

    #create list of lines
    dnslist = dnsfile.readlines()

    #loop over lines
    for dns in dnslist:
        print(dns, end="")

    dnsfile.close() #closing the file
main()
