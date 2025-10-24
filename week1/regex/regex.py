import re
handle  = input('enter file name: ')
fhandle = open(handle)

list = []
for num in fhandle:
    keep = re.findall('[0-9]+', num)
    for answer in keep:
        #answer = int(answer)
        list.append(int(answer))
        new = sum(list)

print(new)        