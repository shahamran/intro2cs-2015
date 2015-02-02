bag= 0
item= 0
gandalf_max= 100
stop_value= -1             #the ring (my precious)
print("Insert weights one by one:")

while item != stop_value:
    #reads the input until a threshold or stop value is reached
    item= int(input())
    #the stop value is the 'ring' and it's weight is -1
    if item == stop_value:
        continue

    elif item<0:            #invalid input, prints error and continues
        print("Weights must be non-negative")
    
    else:                   #correct input, sums the weight
        bag+=item

        if bag>gandalf_max: #checks if the threshold is reached
            print("Overweight! Gandalf will not approve.")
            break          
#this is reached when the stop value is entered
else:
    print("The total packed weight is", bag)
