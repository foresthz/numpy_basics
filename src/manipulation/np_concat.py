'''
Created on 2017-07-31

@author: btws
'''

import numpy as np

list_m = [2,3]
list_n = [4,5]
o = [8,9]

w = np.array([[5,6], [7,8]])

x = np.array([[1,2], [3,4]])

y = np.array([5,6])
z = np.array([[5,6]])

# must use parenthesis
m1 = np.concatenate((list_m,list_n))
print 'm1 : \list_n', m1
# convert to one dimension list?
m2 = np.concatenate((list_m,list_n,o))
print 'm2 : \list_n', m2


m3 = np.vstack((w,x))
m4 = np.vstack((x,w))

print 'm3: \list_n', m3
print 'm4: \list_n', m4

m5 = np.hstack((w,x))
m6 = np.hstack((x,w))

print 'm5: \list_n', m5
print 'm6: \list_n', m6
