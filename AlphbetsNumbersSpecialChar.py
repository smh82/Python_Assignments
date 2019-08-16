# Write a Python program that accepts a string and calculate the number of digits and letters



text = input ("Enter text: ")

numbers=0
characters=0
specialChar=0
spaces=0

for i in text:
    if i.isnumeric()==True:
        numbers+=1
    elif i.isalpha()==True:
        characters+=1
    elif i.isspace()==True:
        spaces+=1
    else:
        specialChar+=1
    
print ( f" numbers= {numbers} \n Alphabets = {characters} \n Special Charactes = {specialChar} \n spaces ={spaces}")  


