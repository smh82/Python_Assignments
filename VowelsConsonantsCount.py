# Input a text and count the occurrences of vowels and consonant


letters = input ("enter the letter to be checked for Consonants and Vowels Count : ")

v = "AEIOU"
cCount=0
vCount=0

for i in letters:
    for j in v:
        if i.upper() == j.upper():
            vCount+=1

cCount= len(letters)-vCount

print(f"count of consonants is {cCount} and count of vowels is {vCount} ")
