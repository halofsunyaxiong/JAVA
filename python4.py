# python面向对象的编程   oop   object  orient ed programming
# 这一部分是python学习的重点。
# 类  对象  方法method   类属性at tribute  类方法method
# 例子

class Student:
#  驼峰命名法 
    def __init__(self,name,score):
        # _int_  是错误的.
        self.name = name
        self.score = score
#   实例属性   
    def say_score(self):
        print('{0}的分数是{1}'.format(self.name,self.score))    
#  实例方法
s1 = Student('tom', 90)
#  实例属性的调用：         实例名称= 类名(参数列表)
s1.say_score()
#  方法调用的格式：         实例名称.方法名称()
#                      解释器的调用实质是：   类名称.方法名称(实例名称)
#  结果  tom的分数是90
# # 构造函数 __init__()
#  通过类名（参数列表）来调用函数时：
#  __new__()   初始化创建的对象，初始化 一般指的是给“实例属性来赋值”。
#  __init__()  用于创建对象，但是我们一般不用输入。
#  python中的self 相当于c++中的指针，

#  类方法的实质是 函数    def __init__(self,形参2,形参3)









# 类对象
class School:
    pass

print(type(School))
print(id(School))
#  <class 'type'>   类对象的type 是“type” 类型，模具类型。 
#  2342402963648


# 类属性attribute
# 类属性的例子

class Person:
    company = 'sxt'
    count = 0
    
    def __init__(self,NAME,SCORE):
        self.NAME = NAME
        self.SCORE = SCORE
        Person.count = Person.count + 1
        
    def say_score(self):
        print('my company is:',Person.company)
        print(self.NAME,'的分数值是：',self.SCORE)
        
s2 = Person('sunyaxiong', 56)
s2.say_score()



s3 = Person('sunyaxiong', 56)
s3.say_score()

s4 = Person('为', 56)
s4.say_score()

s5 = Person('额', 56)
s5.say_score()

s6 = Person('人', 56)
s6.say_score()
print('一共创建{0}个person对象' .format(Person.count))
''' 结果：
my company is: sxt
sunyaxiong 的分数值是： 56
my company is: sxt
sunyaxiong 的分数值是： 56
my company is: sxt
为 的分数值是： 56
my company is: sxt
额 的分数值是： 56
my company is: sxt
人 的分数值是： 56
一共创建5个person对象
'''
#  #   内存原理：
#     先开辟一个 称为   person 的模具对象。
#     person中包含有  类属性（class attribute）  company    count  
#                    类方法 （ class method）    say_SCORE
#                    

