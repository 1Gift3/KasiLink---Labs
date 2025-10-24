fname  = input('enter file:')
if len(fname) < 1 : fname = 'clown.txt'

fhand = open(fname)

many ={}

for line in fhand :
    line = line.strip()
    wds = line.split()

    for w in wds:
        many[w] = many.get(w, 0) + 1

# Finding the top 5 words by frequency
#print(many)
 
#print ((many.items()))

temp = dict()
newlist = []
for k,v in many.items():
    tup = (v,k)
    newlist.append(tup)

cool = sorted(newlist, reverse=True)
#print(cool)

for v,k in cool[:5] :
    print(k,v)


#print(newlist)
#print(sorted(newlist, reverse=True))




