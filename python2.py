# 数据容器   数组 包含多个元素的数字综合
# 






# 👆👆👆👆👆👆list
# 列表的定义格式
# 变量名称 = [元素1,元素2,元素3,元素4,元素5]
# 案例

name_list = ['itheima','itcast','python']
print(name_list)
print(type(name_list))

# 列表的嵌套
# 案例
my_list = [[1,2,3],[4,5,6]]
print(my_list)
print(type(my_list))
# 答案
# [[1,2,3],[4,5,6]]
# <class 'list'>      类型是list


  
  
#  👆👆👆列表的下标索引 
# 下标索引的作用
# 通过下标索引来取出相应位置的元素
# 案例
name_list('tom','rose','lily')
print(name_list[0]) 
# 结果 tom
print(name_list[1]) 
# 结果 rose
print(name_list[2])
# 结果 lily

print(name_list[-1])  
# 结果 lily
print(name_list[-2])  
# 结果 rose 
print(name_list[-3]) 
# 结果 tom

# #🏔️🏔️嵌套列表的索引如何操作
my_list = [[1,2,3],[4,5,6]]
print(my_list[1][1])
# 结果 5


# #🏔️🏔️列表的一系列功能，我们称之为列表的方法。  
# 🇮🇮🇮🇮insert方法    在指定的下标位置插入指定的元素：
# 格式：列表.insert(下标索引值,新的元素值)
# 案例
he_list = [57,78,89]]
he_list.insert(2,23)
print(he_list)
# 结果： [57,78,23,89]








# 删除元素




# 🇮🇮🇮🇮index方法   查询功能列表元素中的下标索引：    # 格式： 列表.index(元素)
# 案例
_list = ['er','ty','yu']
index = _list.index('yu')
print(f"yu在列表_list中的下标索引值是:{index}")
# 结果：   yu在列表_list中的下标索引值是：2
print(f"yuo在列表_list中的下标索引值是:{index}")
# 结果：  ValueError 'yuo' is not in list
# 元素不存在
# 🇮🇮🇮🇮  修改索引所在的元素值：
# 格式： 列表[索引值] = 新的元素值
# 案例
_list = ['er','ty','yu']
_list[0] = 'chinese'
print(f"{_list}")
# 结果： ['chinese','ty','yu']
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  