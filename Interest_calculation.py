# Write a Python program to compute the future value of a specified principal amount, 
# rate of interest, and a number of years

p = float(input("Enter principal amount : "))
i=  float(input("Enter interest % : "))
y = float(input("Enter investment tenure in years  : "))

fv = p * (1+i)**y

print ("After {yy} years your principal amount {pp} over an interest rate of {ii} % will earn {fvv}".format(yy=y,pp=p,ii=i,fvv=fv))