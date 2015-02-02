orc=[]          #a list variable that holds the number of arrows needed to kill
                #an indexed orc.
orc.append(1)   #for example: orc[0] and orc[1] takes 1 arrow to kill.
orc.append(1)
arrows= 0 
orcs= int(input("Which Orc do you wish to confront?"))

#calculates the number of arrows for desired orc
for orc_num in range(2,orcs):
        orc.append(orc[orc_num-1]+orc[orc_num-2])

arrows= orc[orcs-1]
print("The required number of arrows is", arrows)
