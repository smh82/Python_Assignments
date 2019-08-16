# Write a Python program to get the volume of a sphere, please take the radius as input from user


import math
radius =    float (input ("Enter Radius of Sphere:"))
areaOfSphere = (4/3) * math.pi * (radius**3)

print("The volume of Sphere is = " + str (round(areaOfSphere,2)))