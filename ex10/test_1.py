from WordExtractor import *

w = WordExtractor(input("Enter file name: "))
iter1 = iter(w)
print("Enter any key to iterate or type 'exit' to quit.")
while True:
    val = input()
    if 'exit' in val:
        break
    
    print(next(iter1), end = "")

