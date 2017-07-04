# example.py
#
# Examples of simple regular expression substitution

import re

# Some sample text
text = 'UPPER PYTHON, lower python, Mixed Python'

print(  re.findall(r'python' , text , flags=re.IGNORECASE ) )

datepat = re.compile(r'python',flags=re.IGNORECASE)
print ( datepat.findall(text) )






