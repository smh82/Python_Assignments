# Python program to calculate number of days between two dates
import datetime

date1 =  input ( "Enter a date in (dd/mm/yyyy) format:")

# print(date1[6:])
# print(date1[3:5])
# print( date1[:2])

x1= datetime.datetime(int(date1[6:]),  int( date1[3:5]), int(date1[:2]) )

print (x1)


date2 =  input ( "Enter a date in (dd/mm/yyyy) format:")

# print(date1[6:])
# print(date1[3:5])
# print( date1[:2])

x2= datetime.datetime(int(date2[6:]),  int( date2[3:5]), int(date2[:2]) )

print (x2)


print ("There are this many days between the 2 dates :" + str( x2-x1)  )


# dd/mm/yyyy