from decimal import Decimal 
from decimal import localcontext

a = Decimal('1.3')
b = Decimal('1.7')

print(a/b)

with localcontext() as ctx:
    ctx.prec = 50
    print(a/b)

nums = [1.23e+17, 1, -1.23e+17]
print( sum(nums) )
#0.0
import math 
print( math.fsum(nums))
 