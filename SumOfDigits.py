# Write a Python program to calculate the sum of the digits in an integer


n = input ("Enter a positve interger : ") 

sm = 0
for w in n:
    sm+=int(w)
print(f"Sum of digits  {n} is {sm} ")
