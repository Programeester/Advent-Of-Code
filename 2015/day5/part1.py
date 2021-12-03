import re

with open("data.txt", "r") as f:
    words = f.readlines()
    print(len([s for s in words if (re.search(r'([aeiou].*){3,}', s) and re.search(r'(.)\1', s) and not re.search(r'ab|cd|pq|xy', s))]))
