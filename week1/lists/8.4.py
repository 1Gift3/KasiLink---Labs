file = open('romeo.txt').read()
lines = file.split()
#print(lines)
list_words = []

for word in lines :
    if word != list_words:
        list_words.append(word)
        list_words.sort()
        
print(list_words)