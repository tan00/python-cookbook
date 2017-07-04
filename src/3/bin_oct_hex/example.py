
#为了将整数转换为二进制、八进制或十六进制的文本串，可以分别使用 bin() ,oct() 或 hex() 函数：

x = 1234
print( bin(x) )
print( oct(x) )
print( hex(x) )

#如果你不想输出 0b , 0o 或者 0x 的前缀的话，可以使用 format() 函数。

print( format(x,'b') )
print( format(x,'o') )
print( format(x,'x') )

#如果你想产生一个无符号值，你需要增加一个指示最大位长度的值
x = -1234
print( format(2**32 + x, 'x'))

#为了以不同的进制转换整数字符串，简单的使用带有进制的 int() 函数即可
print( int('4d2', 16) )
print( int('-4d2', 16) )
