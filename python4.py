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
s1.say_score()