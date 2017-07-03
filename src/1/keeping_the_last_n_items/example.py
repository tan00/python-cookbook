"""
Docstring  1.3.2保存最后n个元素
"""

from collections import deque
import os

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
    
    os.chdir('keeping_the_last_n_items')
    print(os.getcwd())
    with open('example.py') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)
