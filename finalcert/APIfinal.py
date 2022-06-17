#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests

#APOD = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

def main():
    ## Send HTTPS GET to the API of APOD
    mysource = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    gotresp = requests.get(mysource)
    print(f"API source: {mysource}")
    print(f"HTTP response code: {gotresp.status_code}")
    print(f"HTTP response.text:\n{gotresp.text}")

    ## Decode the response
    #got_dj = gotresp.json()

    ## print the response
    #print(got_dj)

main()
