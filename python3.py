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
def main():
    print("------------------主菜单------------------")
    print(f"{name}，你好，欢迎来到SUN银行，前选择操作：")
    print("查询余额 \t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")     
    print("退出\t\t[输入4]")
    return input("请输入你的选择：")      
# 设置循环函数，确保程序不退出
while True:
    KeyboardInterrupt = main()
    if KeyboardInterrupt =="1":
        query(True)
        continue
    elif KeyboardInterrupt =="2":
        num = int(input("你想要存多少钱，请输入："))
        save(num)
        continue
    elif KeyboardInterrupt =="3":
         num = int(input("你想要取多少钱，请输入："))
         get_money(num)
         continue
    else:
        print("程序推出了")
        break