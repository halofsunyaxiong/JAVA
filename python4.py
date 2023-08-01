# python面向对象的编程   oop   object  orient ed programming
# 这一部分是python学习的重点。
# 类  对象  方法method   类属性  类方法method
# 例子

class Student:
#  驼峰命名法 
    def __init__(self,name,score):
        # _int_  是错误的.
        self.naime = name
        self.score = score
#   属性  
    def say_score(self):
        print('{0}的分数是{1}' .format(self.name,self.score))    

s1 = Student('tom', 90)
#  通过类名（参数列表）来调用函数
s1.say_score()

#  结果  tom的分数是90
# # 构造函数 __init__()
#  通过类名（参数列表）来调用函数时：
#  __new__()   初始化创建的对象，初始化 一般指的是给“实例属性来赋值”。
#  __init__()  用于创建对象，但是我们一般不用输入。
#  python中的self 相当于c++中的指针，

#  类方法的实质是 函数    def __init__(self,形参2,形参3)
