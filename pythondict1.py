#!/usr/bin/env python3

#create a dictionary
switch = {"hostname":"sw1", "ip":"10.0.1.1", "version":"1.2", "vendor":"cisco"}

#display parts of the dictionary
print(switch["hostname"])
print(switch["ip"])

#request a fake key
#print(switch["dog"])


#request a fake key with get method
print("First test - Get method")
print(switch.get("dog"))

print("Second test - Get method")
print(switch.get("dog", "THE KEY IS IN ANOTHER CASTLE"))

print("Third test - Get method")
print(switch.get("version"))


print(switch.keys())
print(switch.values())
