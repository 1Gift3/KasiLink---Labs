"""Assignment: compute average X-DSPAM-Confidence from a file.

Prompts for a filename, reads the file, finds lines that start with
'X-DSPAM-Confidence:', extracts the float after the colon, counts the
matching lines and computes the average. Does not use sum() or a
variable named 'sum'.
"""

fname = input("Enter file name: ").strip()
try:
    fh = open(fname)
except FileNotFoundError:
    print(f"File not found: {fname}")
    raise

count = 0
total = 0.0

for line in fh:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    # Extract numeric part and convert to float
    try:
        num_str = line.split(':', 1)[1].strip()
        number = float(num_str)
    except (IndexError, ValueError):
        # Skip malformed lines silently
        continue
    count += 1
    total += number

fh.close()

print('Count:', count)
print('Total:', total)
if count > 0:
    print('Average spam confidence:', total / count)
else:
    print('Average spam confidence: N/A')
