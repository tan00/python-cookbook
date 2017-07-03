"""
Docstring  1.3.2保存最后n个元素
"""

from collections import deque
import os

def search(lines,pattern,history=5):
    savedeque = deque(maxlen=history)
    for sigleline in lines:
        if pattern in sigleline:
            yield sigleline, savedeque
        savedeque.append(sigleline)

#main
if __name__ == '__main__':
    os.chdir('keeping_the_last_n_items')
    with open('my.py',encoding='utf-8') as fp:
        for line , savelist   in search(fp, 'keeping' , 3):
            for pline in savelist:
                print(pline)
           
