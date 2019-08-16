
import csv
data=[]
with open("D:\PIAIC\Python_Hello_World\myfile.csv","r",) as f:
    data_handler= csv.reader(f)
    for each_line in data_handler:
        data+=each_line
    
print (data)
st = input("what you want to search :" )
print(  data.index(st))

