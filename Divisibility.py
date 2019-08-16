# Python program to check whether a number is completely divisible by another number. 
# Accept two integer values form the user

Numerator = int(input("Enter Numerator"))

Denominator = int(input("Enter Denominator"))

if Numerator%Denominator == 0:
    print ("The number " + str(Numerator) + " is completely Divisible by "+ str(Denominator))
else:
    print ("The number " + str(Numerator) + " is not completely Divisible by "+ str(Denominator))