fname = input("Enter file name: ")
if len(fname) < 1 : fname = 'clown.txt'

fhand = open(fname)

many = dict()

for line in fhand:
    line = line.rstrip()
    #print(line)
    wds = line.split()
    #print(wds)

#print(fname, len(fname) )
    for w in wds:
        #print('===============>',w)
        #print('before', many)

        #OLD WAY
        #oldvl = 0
        #if w in many : oldvl = many[w]
        #NEW WAY (prettier way)
        #oldvl = many.get(w, 0)

        #print('oldvl', oldvl)
        many[w] = many.get(w, 0) + 1
        #print('after', many)

print (many)

# Now finding the word with the largest count

largest = None 
bigword = None
for key, value in many.items() :
    print(key, value)
    if largest is None or value > largest :
        largest = value
        bigword = key
print(bigword, largest)
