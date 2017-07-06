import os 
from collections import defaultdict

os.chdir('./.vscode')

word_summary = defaultdict(list)
with open('launch.json', 'r') as f:
    lines = f.readlines()
for idx, line in enumerate(lines,1):
# Create a list of words in current line
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

print(word_summary)