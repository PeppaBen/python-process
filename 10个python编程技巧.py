#import this
#zen of python




# name='ben'
# country='China'
# age=20

# print('Hi,I am %s,I am from %s,I am %d' %(name,country,age))  #d decimal 十进制格式化字符串
# print('Hi,I am {},I am from {},I am {}'.format(name,country,age))
# print('Hi,I am {0},yes,I am {0}'.format(name))
# print(f'Hi,I am {name},I am {age+1},and I from {country}')   #替换成表达式






# def fibonacci(n):
#     a=0  #代表前一个数
#     b=1  #代表后一个数
#     nums=[]
#     for _ in range(n):
#         nums.append(a)
#         a,b=b,a+b
#     return nums

# for i in fibonacci(10):
#     print(i)

#使用yield语法来替换在list末尾添加元素
# def fibonacci(n):
#     a=0  #代表前一个数
#     b=1  #代表后一个数
    
#     for _ in range(n):
#         yield a  #每当计算出一个元素就立马送出去，外边的for循环就立即输出不需要等待列表生成完后在一个个输出
#         a,b=b,a+b
    

# for i in fibonacci(10):
#     print(i)











#列表生成式的使用
#fruit=['apple','pear','pineapple','orange','banana']

#将水果首字母大写
# for i in range(len(fruit)):
#     fruit[i]=fruit[i].capitalize()  #记得加[i]
# print(fruit)

# fruit=[x.capitalize() for x in fruit]
# print(fruit)

# fruit=[x.capitalize() for x in sorted(fruit)]
# print(fruit)


#过滤列表中首字母为a的水果
# filtered_fruit=[]
# for i in fruit:
#     if i.startswith("A"):
#         filtered_fruit.append(i)
# print(filtered_fruit)


# filtered_fruit=[x for x in fruit if x.startswith("B")]
# print(filtered_fruit)



#enumerate函数  在循环输出时同时得到索引值

# for i in fruit:
#     print(i)

# for i,x in enumerate(fruit):
#     print(i,x)
# print()

#反向遍历
# for i,x in enumerate(reversed(fruit)):
#     print(i,x)
# print()
#正向遍历 按名称顺序排序 使用内置函数sorted()
# for i,x in enumerate(sorted(fruit)):
#     print(i,x)






#字典的合并
# a={'anna':'123','ben':'456'}  #存放用户名及密码
# b={'cindy':'789'}

# c={}
# for k in a:
#     c[k]=a[k]
# for k in b:
#     c[k]=b[k]
# print(c)

# print('********************')
# c={**a,**b}  # **表示解包的意思，直接将a,b中的内容写入c
# print(c)





#三元运算符 ternary operator
#java ...?...:...
# if score>60:
#     s='pass'
# else:
#     s='fail'

# s='pass' if score>60 else 'fail'








#序列解包 sequence unpacking  tuple list range

# name="San Zhang" #存放张三的姓和名  外国人名前姓后
# #单独提取并存放在不同变量中

# str_list=name.split()  #按照空格分割
# first_name=str_list[0]
# last_name=str_list[1]

# print(first_name,last_name)
# print('*************')

# first_name,last_name=name.split()
# print(first_name,last_name)








#with 语句  不用close(),减少系统资源占用

# with open ('a.txt',"r") as t:
#     s=t.read()