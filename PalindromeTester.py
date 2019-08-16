# Write a program to check whether given input is palindrome or not

st = input ("enter text to check : ")

rst =''

for i in range(len(st)):
    rst = rst + st[len(st) - 1 - i]

if st == rst :
    print ( "the text is a palindrome ")
else :
    print ( "the text is not a palindrome ")