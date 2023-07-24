# for 循环的基础语法
# 逐个来循环
# 遍历字符串
# for 循环的格式
# for 变量 in 序列类型：
# for x in run:
# 序列类型指的是 字符串 列表 元组 等；
# 


name = "sunyaxiong"
for x in name:
    print(x)
    
print("---------------------------------------------")

yanan = "chianese"
for y in yanan:
    print(y)


# for 循环是无法定义循环条件的
# 案例
Name = "itheima is a brand of itcast"
count = 0
for u in Name:
    if u == "a":
        count += 1
print(f"字符串中有{count}个a")


# range 语句
# range 语句的格式定义： range(num)
# 获取一个从0 开始，到num结束的数字序列，不含num本身/
# 如 rang(5)  [0,1,2,3,4]
#  rang (num1,num2)
# 如  rang(5,10) [5,6,7,8,9]
# rang(num1,num2,step)
# 获取一个从num1 开始，到num2结束的数字序列，不含num本身.步长为2；step默认是1；
# 如 rang(5,10,2)   [5,7,10]

range(10)

range(1,10)

range(6,10,2)
# 要配合for循环来进行使用



for x in range(10):
    print(x)


for o in range(1,10):
    print(o)
print("-----------------------")
for p in range(1,10,3):
    print(p)

# 在for循环的外部是可以访问临时变量的，在编程规范上是不允许的，但是在实际上是是可以访问的。
# 规范不是严格的限制。
# 临时变量的作用域












# for 循环的嵌套语句
n = 0
for n in range(1,101):
    print(f"这是向小美表白的第{n}天，坚持。")
    
    for g in range(1,11):
        print(f"送给小美的第{g}朵玫瑰花")
    print(f"小美，我喜欢你，第{n}天的表白结束。")
print(f"第{n}天，表白成功。")
    
    


