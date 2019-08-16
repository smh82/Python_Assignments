import json

print("*******************************************************")
print("***************                      ******************")
print("-------------------------------------------------------")
print("***************Alien Invasion - System*****************")
print("******************Alien Conversation*******************")
print("-------------------------------------------------------")
print("******************                    *****************")
print("*******************************************************")


''' for first time only
alinetalk = {
    "hi":"da",
    "hello":"dataaaa",
    "destroy":"des",
    "human":"ha",
    "world":"wa",
    "ruin":"ra",
    "leader":"lad",
    "invasion":"ivna",
    "fire":"fi",
    "blast":"bla",
    "fight":"yu",
}

'''

with open ("AlienDictionary.json","r") as fileread:
    alinetalk= json.load(fileread)

print(alinetalk)

option =  str(input(" *** for Alien Taking Press T | For Adding new vocabulary Press V | Q for quit ***    :"))
print (option )

while option != "Q":
    
    if option == "V" :
        AL = str(input(" *** Enter Alien language **** :"))
        HL = str(input(" *** Enter Human language Equiavalent **** :"))
        alinetalk[HL]=AL
    elif option == "T" :
        AL = str(input(" *** Enter Alien language you want to convert **** :"))
        # print (AL)
        for k,v in  alinetalk.items():
            if v==AL:
             print ("English Meaning is :  "+ k); break
            #else :
             #print ("this is a new word please have it added"); break
        #print (alinetalk)

    option =  str(input(" *** for Alien Taking Press T | For Adding new vocabulary Press V | Q for quit ***    :"))
    print (option )


with open ("AlienDictionary.json","w") as file:
    json.dump(alinetalk,file)

