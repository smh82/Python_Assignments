# Write a Python program that will accept the base and height of a triangle and compute the area

h = float(input ("enter triangle height :"))
b = float(input ("enter triangle base :"))

area = (1/2)*b*h

print("Area of a Triangle with Height {hh} and Base {bb} is ".format(hh=h,bb=b)+str(area))