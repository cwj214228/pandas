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


dt = {
    'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two': pd.Series([4, 5, 6], index=['a', 'b', 'c'])
}
c = pd.DataFrame(dt, index=['a', 'b', 'c'], columns=['two', 'four'])
print(c)
'''
   two four
a    4  NaN
b    5  NaN
c    6  NaN
'''
