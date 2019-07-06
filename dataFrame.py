import pandas as pd
import numpy as np

# d = pd.DataFrame(np.arange(10).reshape(2, 5))
# print(d)
'''
   0  1  2  3  4
0  0  1  2  3  4
1  5  6  7  8  9
'''

# dt = {
#     'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#     'two': pd.Series([4, 5, 6], index=['a', 'b', 'c'])
# }
# c = pd.DataFrame(dt)
# print(c)
'''
   one  two
a    1    4
b    2    5
c    3    6
'''


# dt = {
#     'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#     'two': pd.Series([4, 5, 6], index=['a', 'b', 'c'])
# }
# c = pd.DataFrame(dt, index=['a', 'b', 'c'], columns=['two', 'four'])
# print(c)
'''
   two four
a    4  NaN
b    5  NaN
c    6  NaN
'''


# dl = {
#     'one': [1, 2, 3, 4],
#     'two': [4, 5, 6, 7]
# }
# c = pd.DataFrame(dl, index=['a', 'b', 'c', 'd'])
# print(c)
'''
   one  two
a    1    4
b    2    5
c    3    6
d    4    7
'''

# dl = {
#     '城市': ['北京', '上海', '广州', '深圳', '沈阳'],
#     '环比': [101.5, 101.2, 101.3, 102.0, 100.1],
#     '同比': [120.7, 127.3, 119.4, 140.9, 101.4],
#     '定基': [121.4, 127.8, 120.0, 145.5, 101.6]
# }
# d = pd.DataFrame(dl, index=['c1', 'c2', 'c3', 'c4', 'c5'])
# print(d)
'''
    城市     环比     同比     定基
c1  北京  101.5  120.7  121.4
c2  上海  101.2  127.3  127.8
c3  广州  101.3  119.4  120.0
c4  深圳  102.0  140.9  145.5
c5  沈阳  100.1  101.4  101.6
'''


# .reindex() 能够改变或者重排Series和DataFrame索引
# dl = {
#     '城市': ['北京', '上海', '广州', '深圳', '沈阳'],
#     '环比': [101.5, 101.2, 101.3, 102.0, 100.1],
#     '同比': [120.7, 127.3, 119.4, 140.9, 101.4],
#     '定基': [121.4, 127.8, 120.0, 145.5, 101.6]
# }
# d = pd.DataFrame(dl, index=['c1', 'c2', 'c3', 'c4', 'c5'])
# d = d.reindex(index=['c5', 'c4', 'c3', 'c2', 'c1'])
# print(d)
'''
    城市     环比     同比     定基
c5  沈阳  100.1  101.4  101.6
c4  深圳  102.0  140.9  145.5
c3  广州  101.3  119.4  120.0
c2  上海  101.2  127.3  127.8
c1  北京  101.5  120.7  121.4
'''
# d = d.reindex(columns= ['定基', '同比', '环比', '城市'])
# print(d)
'''
       定基     同比     环比  城市
c1  121.4  120.7  101.5  北京
c2  127.8  127.3  101.2  上海
c3  120.0  119.4  101.3  广州
c4  145.5  140.9  102.0  深圳
c5  101.6  101.4  100.1  沈阳
'''


# dl = {
#     '城市': ['北京', '上海', '广州', '深圳', '沈阳'],
#     '环比': [101.5, 101.2, 101.3, 102.0, 100.1],
#     '同比': [120.7, 127.3, 119.4, 140.9, 101.4],
#     '定基': [121.4, 127.8, 120.0, 145.5, 101.6]
# }
# d = pd.DataFrame(dl, index=['c1', 'c2', 'c3', 'c4', 'c5'])
# nc = d.columns.delete(2)
# ni = d.index.insert(5, 'c0')
# nd = d.reindex(index=ni, columns=nc)
# print(nd)
'''
     城市     环比     定基
c1   北京  101.5  121.4
c2   上海  101.2  127.8
c3   广州  101.3  120.0
c4   深圳  102.0  145.5
c5   沈阳  100.1  101.6
c0  NaN    NaN    NaN
'''

# .drop() 能够删除Series和DataFrame指定行或者索引,运算完后会产生一个新的DataFrame对象
# dl = {
#     '城市': ['北京', '上海', '广州', '深圳', '沈阳'],
#     '环比': [101.5, 101.2, 101.3, 102.0, 100.1],
#     '同比': [120.7, 127.3, 119.4, 140.9, 101.4],
#     '定基': [121.4, 127.8, 120.0, 145.5, 101.6]
# }
# d = pd.DataFrame(dl, index=['c1', 'c2', 'c3', 'c4', 'c5'])
# e = d.drop('c2')
# print(e)
'''
    城市     环比     同比     定基
c1  北京  101.5  120.7  121.4
c3  广州  101.3  119.4  120.0
c4  深圳  102.0  140.9  145.5
c5  沈阳  100.1  101.4  101.6
'''


# a = pd.DataFrame(np.arange(12).reshape(3, 4))
# b = pd.DataFrame(np.arange(20).reshape(4, 5))
# c = a.add(b, fill_value=100)  # 加法运算，没有得相加得数据用100与它们相加
# print(c)
'''
       0      1      2      3      4
0    0.0    2.0    4.0    6.0  104.0
1    9.0   11.0   13.0   15.0  109.0
2   18.0   20.0   22.0   24.0  114.0
3  115.0  116.0  117.0  118.0  119.0
'''
# c = a.mul(b, fill_value=0)  # 乘法
# print(c)
'''
      0     1      2      3    4
0   0.0   1.0    4.0    9.0  0.0
1  20.0  30.0   42.0   56.0  0.0
2  80.0  99.0  120.0  143.0  0.0
3   0.0   0.0    0.0    0.0  0.0
'''

# 数据进行对比，返回的是True或者False，尺寸不同会报错
# a = pd.DataFrame(np.arange(12).reshape(3, 4))
# b = pd.DataFrame(np.arange(12, 0, -1).reshape(3, 4))
# c = a > b
# print(c)
'''
       0      1      2      3
0  False  False  False  False
1  False  False  False   True
2   True   True   True   True
'''
# c = a == b
# print(c)
'''
       0      1      2      3
0  False  False  False  False
1  False  False   True  False
2  False  False  False  False
'''


# .sort_index() 方法再指定轴上根据索引进行排序，默认是升序
# b = pd.DataFrame(np.arange(20).reshape(4, 5), index=['c', 'a', 'd', 'b'])
# c = b.sort_index(ascending=False)  # 倒序排序
# print(c)
'''
    0   1   2   3   4
d  10  11  12  13  14
c   0   1   2   3   4
b  15  16  17  18  19
a   5   6   7   8   9
'''
# c = b.sort_index(axis=1, ascending=False)  # 对1轴进行降序排序
# print(c)
'''
    4   3   2   1   0
c   4   3   2   1   0
a   9   8   7   6   5
d  14  13  12  11  10
b  19  18  17  16  15
'''


# .sort_values() 在指定轴上根据数据进行排序，默认升序
# b = pd.DataFrame(np.arange(20).reshape(4, 5), index=['c', 'a', 'd', 'b'])  # 对第二列的数据进行了降序的排序
# c = b.sort_values(2, ascending=False)
# print(c)
'''
    0   1   2   3   4
b  15  16  17  18  19
d  10  11  12  13  14
a   5   6   7   8   9
c   0   1   2   3   4
'''
# c = b.sort_values('a', ascending=False, axis=1)  # 对“a”行进行降序的排序
# print(c)
'''
    4   3   2   1   0
c   4   3   2   1   0
a   9   8   7   6   5
d  14  13  12  11  10
b  19  18  17  16  15
'''