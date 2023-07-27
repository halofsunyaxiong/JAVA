# Python的文件读取
# 格式  定义变量名 = open('文件名',编码方式 = ' ')
#.    定义变量名1 = 定义变量名.read()
#   print(定义变量名1)
#   定义变量名.colse()
#. 例文
file = open('我爱Python.txt', encoding = 'urf-8')
content = file.read()
print(content)
file.close()