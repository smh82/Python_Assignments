# write a Python program to compute the distance between the points (x1, y1) and (x2, y2)

x1, y1=input ( " enter first cordinate " )

print( f" first cordinate is {x1,y1} " )

x2, y2=input(" enter second cordinate ")

print(f" second cordinate is {x2,y2} ") 

distance = ( (int(x2)-int(x1))**2 + (int(y2)-int(y1))**2 ) ** 1//2

print ("the distance between the 2 points is :"+ str(distance))