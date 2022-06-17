#!/usr/bin/env python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests

AOIF = "https://www.anapioficeandfire.com/api"

def main():
    #Send HTTPS GET to the API of ICE and Fire
    gotresp = requests.get(AOIF)
    
    #Decode the response - convert file to json
    decresp = gotresp.json()

    #print the response
    print(decresp)

main()


