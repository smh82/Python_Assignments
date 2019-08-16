
#Write a python program to sum of the first n positive integers

n = int( input ("Enter a positve interger : ") )
sm = 0
for w in range(0,n+1):
    sm+=w
print(f"Sum of n Positive integers till {n} is {sm} ")
