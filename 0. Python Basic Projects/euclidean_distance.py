'''
(Wikipedia)
In mathematics, the Euclidean distance between two points in a Euclidean space is the length of the line segment between them. 
It can be calculated from the Cartesian coordinates of the points using the Pythagorean theorem, 
and therefore is occasionally called the Pythagorean distance.
'''

import math

a = (3, 4)
o = (0, 0)
x = (a[0] - o[0])**2
# print('x = ', x)
y = (a[1] - o[1])**2
# print('y = ', y)
z = x + y
# print('z = ', z)
euc_dis = math.sqrt(z)
print(euc_dis)