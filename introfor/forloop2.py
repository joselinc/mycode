#!/usr/bin/env python3

def main():
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    for farm in farms:
        print(farm.get("name"), "has", end=":\n")
        for items in farm.get("agriculture"):
            print(" -", items)
    print("\nThis is the end of the loop.")

main()
