# Write a Python program to get a string which is n (non-negative integer) copies of a given string.


string = input( "Enter your string that you want to print n times : ")
n=int(input("enter n time :"))


for i in range (1, n+1):
    print( string,end = " ")

