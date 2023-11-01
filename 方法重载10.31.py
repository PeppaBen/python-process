# #重写父类方法
# class Father:
#     money=1000000
#     __money=100000011

#     def drive(self):
#         print("I can drive")

# class Mother:
#     money=1000001

# class Son(Father,Mother):  #继承在括号里写父类
   
#     def pay(self):
#         print(self.money)

#     def drive(self):
#         print("I can drive tank")
#         Father.drive(self)  #记得加self调用父类

# Tom=Father()
# Jerry=Son()

# Tom.drive()
# Jerry.drive()



class MyList:
    __mylist=[] #私有化,内部传值，不希望别人用到

    def __init__(self,*args):
        self.__mylist=[] 
        for arg in args:
            self.__mylist.append(arg)


    def __add__(self,x):
        for i in range(0,len(self.__mylist)):
            self.__mylist[i]=self.__mylist[i]+x #错多了
        return self.__mylist

    def __sub__(self,x):
        pass

    def __mul__(self,x):
        pass

    def show(self):
        print(self.__mylist)

    def len(self):
        pass

    def mod(self):
        pass
    

if __name__=='__main__':
    l=MyList(1,2,3,4,5)
    # x=l+10      #用return方法返回值，实例化对象接收可重复使用
    # print(x)
    l+10
    l.show()