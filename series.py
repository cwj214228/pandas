import pandas as pd


# “index=”可以省略
# a = pd.Series([5, 56, 80])
# print(a)

# “index=”不能省略
# b = pd.Series(25, index=['a', 'b', 'c'])
# print(b)

# 从字典中创建
# dct = {'a': 1, 'b': 2, 'c': 3}
# c = pd.Series(dct)
# print(c)

# 从字典中创建
# dct = {'a': 1, 'b': 2, 'c': 3}
# c = pd.Series(dct, index=['a', 'b', 'c', 'd'])
# print(c)
# print(c[:3])
# print('a' in c)  # 索引存在，就返回True
# print(c.get('b', 100))  # 能获得“b”的值，就返回对应的value，没有就输出100

# 索引一样的才能进行运算
# a = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
# b = pd.Series([2, 3, 4], index=['b', 'c', 'd'])
# c = a + b
# print(c)
'''
a    NaN
b    4.0
c    6.0
d    NaN
'''

a = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
a.name = 'Series对象'
a.index.name = '索引列'
print(a)
'''
索引列
a    1
b    2
c    3
Name: Series对象, dtype: int64
'''



