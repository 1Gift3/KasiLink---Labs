name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

dyct = dict()

for line in handle :
    if line.startswith("From "):
        line = line.rstrip()
        words = line.split()
        time = words[5]
        hour_split = time.split(':')
        hour = hour_split[0]
        dyct[hour] = dyct.get(hour, 0) + 1

for k,v in sorted(dyct.items()):
    print(k,v)