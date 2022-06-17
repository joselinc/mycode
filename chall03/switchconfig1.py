#!/usr/bin/env python3

import time
import os
import yaml
import crayons

def switchcount(switches):
    i = 0
    for switch in switches:
        i += 1
    return i


def switchstatus():
    with open("switchconfig", "r") as switchdata:
        myswitches = yaml.safe_load(switchdata)

        print(crayons.red(f"There are {switchcount(myswitches)} switches to configure", bold=True))
        
        for switch in myswitches:
            print(crayons.white(f"\nConnecting to {switch.get('switchname')} via {switch.get('sshtarget')} ", bold=True))
            for i in range(8):
                time.sleep(.25)
                print(crayons.yellow(".", bold=True))
            print(crayons.green("Connected!", bold=True))
            for commands in switch.get('commands'):
                print(crayons.blue(f"Sending: {commands.get('command')} {commands.get('subcommand')}", bold=True))
            time.sleep(2)       

def main():
    switchstatus()
main()

