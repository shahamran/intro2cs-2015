smallest=0
smallest_pos=0
second=0
second_pos=0
num_of_dancers=10
dancers=range(num_of_dancers)

for dancer in dancers:
    #Gets the age for each dancer (from input)
    age=int(input("What is the age of the current dancer?"))

    #Checks if this dancer is smaller then the smallest so far
    if age<smallest or smallest==0:  #or if it's the first run.
        second=smallest              #'second' gets the old 'smallest' values
        second_pos=smallest_pos
        smallest=age
        smallest_pos=dancer+1

    #checks which is the smallest EXCLUDING the smallest (second smallest)
    if age<second and age>smallest or second<=smallest: 
        second=age
        second_pos=dancer+1

#prints the output
print("Pippin is dancer number",second_pos)


