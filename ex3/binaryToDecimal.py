num_in= int(input("Insert number in binary representation:"))

from_base= 2
to_base= 10

num_out= 0
stop= False
pos= 0 #holds number of digit in the composed number
       #we are currently checking.

#a loop that goes through every figure in the input number
#to convert it to chosen base (decimal in this case)
while stop == False:
    if num_in // to_base == 0: stop= True
    num_out+= (num_in % to_base) * (from_base ** pos)
    num_in//= to_base
    pos+= 1
        
print("The decimal value of the inserted binary number is", num_out)
