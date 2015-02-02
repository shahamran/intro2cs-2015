from WordTracker import *
lst = []
print("Enter dictionary words, one by one and enter 'end' in the end")
word = ""
while word != 'end':
    word = input()
    if word != 'end': lst.append(word)
w = WordTracker(lst)
print("Enter words to search: ")
word = ''
while word != 'end':
    word = input()
    if word != 'end': print(w.encounter(word))
print(w.encountered_all())
