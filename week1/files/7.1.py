fh  = open('mbox-short.txt')
print(fh)

for line in fh :
    lines = line.rstrip().upper()
    print (lines)