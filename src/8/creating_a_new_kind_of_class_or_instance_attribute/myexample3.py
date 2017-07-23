#描述器解释
#Python 有三个特殊方法，__get__、__set__、__delete__，用于覆盖属性的一些默认行为，
# 如果一个类定义了其中一个方法，那么它的实例就是描述器

#描述器是一种代理机制，对属性的操作由这个描述器来代理
#访问: __get__(self, instance, cls) # instance 代表实例本身，cls 表示类本身，使用类直接访问时，instance 为 None
#赋值: __set__(self, instance, value) # instance 为实例，value 为值
#删除: __delete__(self, instance) # instance 为实例

class Descriptor:
    def __init__(self, initvar=None, name='var'):
        self.initvar = initvar
        self.name = name
        
    def __get__(self, instance, cls):
        print('Get', self.name, 'instance=',instance, 'cls=',cls)
        return self.initvar
    
    def __set__(self, instance, value):
        print('Set', self.name, value)
        self.initvar = value
    
class E:
    a = Descriptor(10, 'a')
    b = Descriptor(20, 'b')


if __name__ == '__main__':
    e = E()
    e.a  

    e.a = 30
