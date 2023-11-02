from functools import reduce

def myadd(a,b):
    return a+b

print(reduce(myadd,[1,2,3,4,5]))

Myadd=lambda x,y:x+y
print(Myadd(1,2))

#只用一次，减少函数定义 只用一次函数的时候用它
#reduce 用help(reduce) 函数+序列
#先将前两个元素相加，然后依次遍历序列相加
#序列处理函数：filter() zip() map() reduce()
#filter()和map()需要list的帮助才能打印

print(reduce(lambda x,y:x+y,[1,2,3,4,5]))

foo=[2,14,6,68,34,25]

print(list(filter(lambda x:x%3==0,foo)))

#对列表每一个元素进行操作使用map

print(list(map(lambda x:x*2+10,foo)))
