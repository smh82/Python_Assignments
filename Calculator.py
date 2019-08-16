# Simple calculator 

First_Number = int(input ("Enter First NUmber") )
Second_Number = int(input ("Enter Second NUmber") )

Operator = input ("Enter Operator : + - / * : ") 

if Operator == "+" :
    print ( str(First_Number+Second_Number) )
elif Operator=="-":
    print ( str(First_Number-Second_Number) )
elif Operator=="*":
    print ( str(First_Number*Second_Number) )
elif Operator=="/":
    print ( str(First_Number/Second_Number) )
else:
    print("you have entered an invalid operator")










