#a range for the loop
riders=range(int(input("Enter the number of riders:"))) 
high_hat=0
gandalf_pos=0

#This is the loop that goes through every hat size and
#checks which is the largest.
for rider in riders:
    height=float(input("How tall is the hat?"))
    if height>high_hat:
        high_hat=height
        gandalf_pos=rider+1                              

print("Gandalf's position is:",gandalf_pos)
