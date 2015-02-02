from_base=int(input("Insert source base (2-10): "))
to_base=int(input("Insert desired base (2-10): "))

num_in=int(input("Insert number in base " + str(from_base) + " representation: "))
out=0
stop=False
pos=0
#goes through every figure in the input number
#to convert it to chosen base
while stop==False:
    if num_in//to_base==0: stop=True
    out+=(num_in%to_base)*(from_base**pos)
    num_in//=to_base
    pos+=1
        
print("The value of the inserted number in base", to_base, "is", out)
