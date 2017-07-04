import random 

values = [1, 2, 3, 4, 5, 6]
#从序列中随机取出一个值
random.choice(values)

#从从序列中随机取出n个值
random.sample(values , 3)
#打乱序列顺序 
random.shuffle(values)

#生成随机整数
print ( random.randint(0,10) )
print ( random.randint(0,10) )
#生成0到1的随机浮点数
random.random()
#获取 N 位随机位 (二进制) 的整数
random.getrandbits(200)
