gimli= int(input("Insert composed number:")) #gets Gimli's input
stop= False
day= 0
goblets= 0
#this loop decomposes the input number for it's decimal figures by division
#(reads the composed number, figure by figure and prints each figure)
while stop == False:
    if gimli// 10 == 0: stop= True
    goblets= gimli % 10
    gimli//= 10
    day+= 1
    print("The number of goblets Gimli drank on day", day, "was",goblets)
