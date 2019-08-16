# Write a Python program to test whether a passed letter is a vowel or not

letter = input ("enter the letter to be checked : ")

v = "AEIOU"

for i in v:
    if i.upper() == letter.upper():
        print("the letter {t}  is a vowel".format(t=letter))
        break
else :
    print( "the letter {t} is not a vowel ".format(t=letter))
