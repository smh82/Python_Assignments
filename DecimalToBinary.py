
# Write a Python program to convert an decimal integer to binary

d = int( input( "Enter Deimal interger to be converted to Binary "))

d1=d

r=0
q=0
b=''

while d != 0 :
    q=d // 2
    r=d % 2
    b=str(r)+b
    d=q

print (f"the binary conversion of {d1} is = " + b)
