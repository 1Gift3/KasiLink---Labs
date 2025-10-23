fname  = input('enter file:')
if len(fname) < 1 : fname = 'clown.txt'

fhand = open(fname)

many ={}

for line in fhand :
    line = line.strip()
    wds = line.split()

    for w in wds:
        many[w] = many.get(w, 0) + 1

# Finding the word with the largest count

largest = None 
bigword = None
for key, value in many.items():
    if largest is None or value > largest :
        largest = value
        bigword = key
        
print(bigword, largest)
                