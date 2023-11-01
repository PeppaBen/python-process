class Father:
    money=1000000
    __money=100000011

    def drive(self):
        print("I can drive")

class Mother:
    money=1000001

class Son(Father,mother):  #继承在括号里写父类
    pass #继承父类的，自己啥也没有
         #公有方法可以继承，私有方法不可以
         #可以继承多个类,如果两个父类有同一个方法属性，只继承第一个
    def pay(self):
        print(self.money)


Tom=Father()
print(Tom.money)
Tom.drive()

print("*"*20)

Jerry=Son()
print(Jerry.money)
Jerry.drive()
Jerry.pay()
