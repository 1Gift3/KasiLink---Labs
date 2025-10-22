"""Read an mbox file, count sendeWrite a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.rom lines starting with 'From ',
and print the most frequent sender and its count.
"""

fname = input("Enter file name (default: mbox-short.txt): ").strip()
if len(fname) < 1:
    fname = 'mbox-short.txt'

try:
    fh = open(fname)
except FileNotFoundError:
    print(f"File not found: {fname}")
    raise

counts = {}
for line in fh:
    if not line.startswith('From '):
        continue
    parts = line.split()
    if len(parts) < 2:
        continue
    mail = parts[1]
    counts[mail] = counts.get(mail, 0) + 1

fh.close()

best_mail = None
best_count = 0
for mail, count in counts.items():
    if count > best_count:
        best_count = count
        best_mail = mail

if best_mail:
    print(best_mail, best_count)
else:
    print("No senders found.")