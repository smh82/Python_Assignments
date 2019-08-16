
print ("                                                  ")
print ("                                                  ")
print ("                                                  ")

English = int(input("Enter Marks Obtained in English"))
Urdu = int(input("Enter Marks Obtained in Urdu"))
Pakistan_Studies = int(input("Enter Marks Obtained in Pakistan Studies"))
Mathematics = int(input("Enter Marks Obtained in Mathematics"))
Physics = int(input("Enter Marks Obtained in Physics"))
Chemistry = int(input("Enter Marks Obtained in Chemistry"))

print ("                                                  ")
print ("                                                  ")

print ("**************************************************")
print ("**************************************************")
print ("         Board of Intermediate Education")
print ("                  Marksheet")
print ("              Annual Examiation")
print("                     Part I")
print("                 Year 1999-2000")
print ("**************************************************")
print ("**************************************************")

print ("                                                  ")
print ("                                                  ")




print ("Subject " + "--------" + "Total Marks" + "--------" + "Marks Obtained")
print ("                                                  ")
print ("English         " + "--------" + str(100) + "--------" +str(English))
print ("Urdu            " + "--------" + str(100) + "--------" +str(Urdu))
print ("Pakistan Studies" + "--------" + str(100) + "--------" +str(Pakistan_Studies))
print ("Mathematics     " + "--------" + str(100) + "--------" +str(Mathematics))
print ("Physics         " + "--------" + str(100) + "--------" +str(Physics))
print ("Chemistry       " + "--------" + str(100) + "--------" +str(Chemistry)) 
print ("                                                  ")
print ("                                                  ")
Total_Marks_Obtained = English+Urdu+Pakistan_Studies+Mathematics+Physics+Chemistry
print ("Total           " + "--------" + str(600) + "--------" +str(Total_Marks_Obtained))
print ("                                                  ")
Percentage = Total_Marks_Obtained/600

if Percentage >=0.8 :
    print ("Grade : A")
elif Percentage >=0.7 and Percentage<0.8:
    print ("Grade : B")
elif Percentage >=0.6 and Percentage<0.7:
    print ("Grade : C")
elif Percentage >=0.5 and Percentage<0.6:
    print ("Grade : D")
else:
  print ("Grade : FAIL")

print ("                                                  ")
print ("                                                  ")
print ("**************************************************")