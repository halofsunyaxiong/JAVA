# 👆👆01两数之和
number1 =1.5
number2 =12
sum = number1 + number2
print(f'The sum of two numbers are:{number1}+{number2}={sum}')

# 👆👆阶乘
def get_jc(number):
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return result
print('阶乘6的值为:',get_jc(6))
print('阶乘50的值为:',get_jc(50))
print('阶乘100的值为:',get_jc(100))

'''
阶乘6的值为: 720
阶乘50的值为: 30414093201713378043612608166064768844377641568960512000000000000
阶乘100的值为: 93326215443944152681699238856266700490715968264381621468
'''
# 👆👆求一个圆的面积
import math
    #  引入一个math文件库
def compute_area_of_circle(r):
    return round(math.pi* r * r,2)
# round 保留小数的位数
print(compute_area_of_circle(3))
print(compute_area_of_circle(7))
print(compute_area_of_circle(15))

# 👆👆区间内的素数列表primes

for i in range(11,25+1):
   print(i)
#    if a % 2 == 0:
#        print('不是素数')
#    else:
#        print('是素数')  





#
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 