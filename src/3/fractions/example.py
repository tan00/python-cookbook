from fractions import Fraction
a = Fraction(5, 4)
b = Fraction(7, 16)

print( a )
print( a.numerator )
print( a.denominator )

print( a + 2)
print( float(a+2) )

c = a*b
print( c )
#limit_denominator 传入分母最大值,返回最接近的分数
print(c.limit_denominator(8))

#as_integer_ratio 返回分数比,为元组,可用于构造分数
f = 3.75
Fraction( *f.as_integer_ratio() )
print( f.as_integer_ratio() )

