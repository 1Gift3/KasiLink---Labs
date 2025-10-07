str = 'X-DSPAM-Confidence: 0.8475 '


found = str.find (':')
print(found)
sliced = str[found+1:]
print(sliced)
finded = float(sliced)
print(finded)