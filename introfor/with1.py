#!/usr/bin/env python3
  
def main():
    #open file in read mode
    with open("dns_servers.txt", "r") as dnsfile:
        #indent to keep the dnsfile object open
        #loop across the lines in the file
        for server in dnsfile:
            server = server.rstrip("\n") #remove newline char if exists
            #if the string server ends with the word 'org'
            if server.endswith("org"): #boolean expression
                with open("org-domain.txt", "a") as serverfile:  # 'a' is append mode
                     serverfile.write(server + "\n")
            # ELSE-IF the string svr ends with 'com'
            elif server.endswith("com"):
                with open("com-domain.txt", "a") as serverfile:  # 'a' is append mode
                    serverfile.write(server + "\n")

main()
