# Write a Python program to calculate body mass index

weight= float(input("Enter weight :"))

height= float(input("Enter height :"))

m=height/100

bmi = weight / (m**2)

print(f" your BMI - {bmi}") 