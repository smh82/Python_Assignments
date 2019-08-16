
# Write a program to convert binary number to Decimal number

b =  input( "Enter Binary to be converted to Deimal interger ") 

d=0

for i in range (len(b)):
    d=d+(int(b[len(b)-1-i]))*(2**i)
    

print (f"the Decimal conversion of {b} is = " + str(d))
