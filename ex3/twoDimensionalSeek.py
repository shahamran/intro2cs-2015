position=[0,0]
heading=0 #I will choose 4 directions: 0,90,180,270
          #for forward,right,backward,left accordingly.
turn=""
steps=0
end_value= "end"
#loop that runs until end value is entered
while turn != end_value:
    turn=input("Next turn:")
    #checks if end value is reached
    if turn == end_value: continue
    #decides how to change the heading
    if turn=="right":
        heading+=90           
    elif turn=="left":
        heading-=90

    heading%=360 #360=0,450=90 etc...

    steps=int(input("How many steps?"))

    #checks the direction to decide how to manipulate the position variable.
    #forward/backward: only y value is changed
    #left/right: only x value is changed

    if heading == 0:         #forward case
        position[1]+= steps 
    elif heading == 180:     #backward case
        position[1]-= steps 
    elif heading == 90:      #right case
        position[0]+= steps
    elif heading == 270:     #left case
        position[0]-= steps

#Gandalf's direction:[right/left,forward/backward]
gandalf_dest=["right","forward"]  

#Checks what needed to be written on the output.
if position[0]>=0:
    gandalf_dest[0]="right"
else:
    gandalf_dest[0]="left"

if position[1]>=0:
    gandalf_dest[1]="forward"
else:
    gandalf_dest[1]="backward"

#changes the output to a positive number.
position[0]=abs(position[0])
position[1]=abs(position[1]) 
   
print("Gandalf should fly",position[0],"steps",gandalf_dest[0],\
                  "and" , position[1] , "steps" , gandalf_dest[1])     
