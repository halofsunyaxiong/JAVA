# 👆👆MySQL入门
# DBMS 数据库管理系统
>>sql 关联式数据库  例子mysql    简称rdbms

>>nosql 非关联性数据库  例子redis   简称nrdbns



orm 思想
orm object retional mapping 数据库中的一个表，对应python中的一个类。
表中的的一条数据，和Java或者python中的一个实体相对应。























# cmd>>MySQL _uroot _proot
# show databases; 查看所有数据库
# use mydata; 进入mydata的数据库
# show tables; 查看mydata数据库的所以表格
# select * from dish; 查看表格中的dish数据的全部；
# desc emp;
# select version(); 查看mysql的版本。
# select * from weather;  显示weather中的全部数据。
# select men,women,girl,boy,spring,summer from weather;  显示weather中men,women,girl,spring,summer的数据。


# exit;    退出数据库
# create database good;  创建一个good数据库
# source c://desktop/sol.sql  导入在电脑桌面的sol.sql的数据表格
# select boy as boys from weather；  临时将boy修改为boys
# select women as "r tt" from weather;临时将women修改为r tt 有空格时，直接将用“ 内容 ”。
#   weather中的fall全部乘数8 得到的值。
<<<<<<< HEAD
# select fall*8 from weather;  
| fall*8 |
+--------+
|     72 |
|     64 |
|     72 |
|      8 |
|     48 |
+--------+
5 rows in set (0.00 sec)
=======

<<<<<<< HEAD
# select fall*12 yearshall from weather;
+-----------+
| yearshall |
+-----------+
|       108 |
|        96 |
|       108 |
|        12 |
|        72 |
+-----------+
5 rows in set (0.00 sec)
=======

# 条件判断和大小的比较。选择出符合大小条件的数据。
# select men,girl,fall from weather where fall >= 6;
+------+------+------+
| men  | girl | fall |
+------+------+------+
|    3 |    5 |    9 |
|    1 |    6 |    8 |
|    4 |   56 |    9 |
|   12 |   34 |    6 |
+------+------+------+
4 rows in set (0.00 sec)
<!-- 在数据库中将and 条件都符合的数据都取出来。 -->
#  select men,girl,fall from weather where fall>= 6 and fall<=8;
<!-- select men,girl,fall from weather fall between 6 and 8;-->
+------+------+------+
| men  | girl | fall |
+------+------+------+
|    1 |    6 |    8 |
|   12 |   34 |    6 |
+------+------+------+
2 rows in set (0.00 sec)




#  select men,women,girl,boy,spring,summer,fall,winter from weather where girl is null;
+------+-------+------+------+--------+--------+------+--------+
| men  | women | girl | boy  | spring | summer | fall | winter |
+------+-------+------+------+--------+--------+------+--------+
|    4 |  NULL | NULL |    0 | y      |        |    8 |      9 |
+------+-------+------+------+--------+--------+------+--------+
1 row in set (0.00 sec)

# 根据条件girl is null 在数据表中筛选出符合条件的数据。
# or 条件语句，进行比较。or 只适用于同一个字的语句，   and 只适用于不同的字段。
and or 的优先级进行比较
or 的优先级别是要大于and 的优先级别的



# in 的运用，fall in(8,6)
# not in的运用  fall not in(8,6)

select * from weather where fall in(8,6); 表示的是fall **等于** 8，6的数来直接筛选出来。


+------+-------+------+------+--------+--------+------+--------+
| men  | women | girl | boy  | spring | summer | fall | winter |
+------+-------+------+------+--------+--------+------+--------+
|    1 |     1 |    6 |    6 | hj     | 9      |    8 |      0 |
|    4 |  NULL | NULL |    0 | y      |        |    8 |      9 |
|   12 |    23 | NULL |    5 | 6      | 6      |    6 |      6 |
+------+-------+------+------+--------+--------+------+--------+
3 rows in set (0.00 sec)

select * from weather where fall not in(8,6);    表示的是fall **不等于** 8，6的数来直接筛选出来。


+------+-------+------+------+--------+--------+------+--------+
| men  | women | girl | boy  | spring | summer | fall | winter |
+------+-------+------+------+--------+--------+------+--------+
|    3 |     4 |    5 |    6 | 7      | 7      |    9 |      0 |
|    2 |     3 |    2 |    1 | 1      | 3      |    1 |      3 |
+------+-------+------+------+--------+--------+------+--------+
2 rows in set (0.00 sec)


# select * from weather;
+------+-------+------+------+--------+--------+------+--------+
| men  | women | girl | boy  | spring | summer | fall | winter |
+------+-------+------+------+--------+--------+------+--------+
|    3 |     4 |    5 |    6 | 7      | 7      |    9 |      0 |
|    1 |     1 |    6 |    6 | hj     | 9      |    8 |      0 |
|    4 |  NULL | NULL |    0 | y      |        |    8 |      9 |
|    2 |     3 |    2 |    1 | 1      | 3      |    1 |      3 |
|   12 |    23 | NULL |    5 | 6      | 6      |    6 |      6 |
+------+-------+------+------+--------+--------+------+--------+
5 rows in set (0.00 sec)



# mysql 中的模糊查询。




