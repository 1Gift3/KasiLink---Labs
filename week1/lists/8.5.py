fhandle = open('mbox-short.txt')

#document = open(fhandle)

email_list = list()

for line in fhandle:
    if line.startswith ("From "):

        whole_line = line.split()
        Newmail = whole_line[1]
        email_list.append(Newmail)

for string in email_list:
    print(string)

print("There were", len(email_list), "lines in the file with From as the first word")
