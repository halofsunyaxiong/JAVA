# Python的文件读取
# 格式  定义变量名 = open('文件名',编码方式 = ' ')
#.    定义变量名1 = 定义变量名.read()
#   print(定义变量名1)
#   定义变量名.colse()
#. 例文


# file = open('mysql.md', encoding = 'urf-8')
# content = file.read()
# print(content)
# file.close()
# python的文件写入


# 👆👆👆👆👆👆函数的进阶
# 函数的综合案例
# 银行系统的atm的构建


# 定义全局变量mony 和 name 
money = 5000000;
name = None
# 完成客户姓名的输入工作
name = input("请你输入你的账户姓名：")

# 定义查询余额函数
def query(header):
    if header:
            print("------------------查询余额------------------")
    print(f"{name}，你好，你的账户余额为{money}元")


# 定义存款函数
def save(num):
    global money
    money += num
    print("------------------存款------------------")
    print(f"{name}，你好，你存款{num}元成功")
    query(False)
# 定义取款函数
def get_money(num):
    global money
    money -= num
    print("------------------取款------------------")
    print(f"{name}，你好，你取款{num}元成功。")
    query(False)
    
# 主菜单函数
def():
    print((f"{name}，你好，欢迎来到SUN银行，前选择操作：")
          