# example.py
#
# Example of splitting a string on multiple delimiters using a regex

import re

line = 'asdf fjdk; afed, fjek,asdf,      foo'

# (a) Splitting on space, comma, and semicolon
# [;,\s]\s* 匹配 ; , 空白 任意次
parts = re.split(r'[;,\s]\s*', line)
print(parts)

# (b) Splitting with a capture group
#匹配; , 空白 任意次 并捕获这些字符
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
#匹配; , 空白 任意次 并放弃这些字符
#fields = re.split(r'(?:;|,|\s)\s*', line)
#print(fields)

# (c) Rebuilding a string using fields above
values = fields[::2]
delimiters = fields[1::2]
delimiters.append('')
print('value =', values)
print('delimiters =', delimiters)
newline = ''.join(v+d for v,d in zip(values, delimiters))
print('newline =', newline)

# (d) Splitting using a non-capture group
parts = re.split(r'(?:,|;|\s)\s*', line)
print(parts)

