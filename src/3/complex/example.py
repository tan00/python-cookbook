# 复数可以用使用函数 complex(real, imag) 或者是带有后缀 j 的浮点数来指定

a = complex(2, 4)
b = 3 - 5j

#可以直接使用常见操作
a.conjugate()
print( a.conjugate() )
print( a+b )
print( a-b )
print( a/b )
print( a*b )
print( abs(a) )

#如果要执行其他的复数函数比如正弦、余弦或平方根，使用 cmath 模块
import cmath
print( cmath.sin(a) )


import numpy
a = numpy.array([2+3j, 4+5j, 6-7j, 8+9j])
print( a+2 )
print( numpy.sin(a) )

#Python 的标准数学函数确实情况下并不能产生复数值，因此你的代码中不可能会出现复数返回值
#如果你想生成一个复数返回结果，你必须显示的使用 cmath 模块，或者在某个支持复数的库中声明复数类型的使用

print( cmath.sqrt(-1) )
