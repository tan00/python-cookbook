#同时指定宽度和精度的一般形式是 '[<>ˆ]?width[,]?(.digits)?'
# 其中 width和 digits 为整数，？代表可出现0次或多次


x = 1234.56789

#两位精度 
print( format(x, '0.2f') )
#'1234.57'

#右对齐
print( format(x, '>10.3f') )
#'  1234.568'

#左对齐
print( format(x, '<10.3f') )
#'1234.568'

#居中
print( format(x, '^10.3f') )
#' 1234.568'

#千分符
print(format(x, ','))
#'1,234.56789'

#千分符 一位精度
print(format(x, '0,.1f'))
#'1,234.6'

#指数记法
print(format(x, '0.3e'))
#'1.235e+03'


