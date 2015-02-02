num_in= int(input("Insert number in decimal representation:"))

from_base= 10
to_base= 2

num_out= 0
stop= False
pos= 0 #holds number of digit in the composed number
       #we are currently checking.

#a loop that goes through every figure in the input number
#to convert it to chosen base (binary in this case)
while stop == False:
    if num_in // to_base == 0: stop= True
    num_out+= (num_in % to_base) * (from_base ** pos)
    num_in//= to_base
    pos+= 1
        
print("The binary value of the inserted decimal number is", num_out)
