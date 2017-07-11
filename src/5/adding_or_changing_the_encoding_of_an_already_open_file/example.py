# Example of adding a text encoding to existing file-like object

import urllib.request
import io

u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()

with open('www.python.org.html','wt')as file:
    file.write(text)


print(text)

