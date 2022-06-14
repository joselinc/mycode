#!/usr/bin/env python3

#combine string

greeting = "Hello! It's good to see you"

name = "Bob"

cc = greeting + " " + name

print(cc)


# .format 

fm = ("{} {}".format(greeting, name))

print(fm)

#f-string

ff = f"{greeting.lower()} {name}"

print(ff)
