#!/usr/bin/env python3
import shutil
import os

def main():
    os.chdir('/home/student/mycode/')
    shutil.move('raynor.obj', 'storage/')

    # program will pause while we accept input
    xname = input('What is the new name for kerrigan.obj? ')
    shutil.move('storage/kerrigan.obj', 'storage/' + xname)

main()
