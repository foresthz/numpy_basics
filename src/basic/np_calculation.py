'''
Created on 2017-06-25

@author: btws
'''

import numpy as np

mat = np.arange(0,27,1)

print 'original mat: '
print mat

a = mat.reshape((3,3,-1))
print 'layout of a: \n', a

# default sum only works on list, and not support matrix

# [[[ analysis, from 0 to 2
# basic element is treated as matrix
print 'sum on axis 0: \n', np.sum(a, axis=0)

# basic element is treated as list
print 'sum on axis 1: \n', np.sum(a, axis=1)

# basic element is treated as single digit
print 'sum on axis 2: \n', np.sum(a, axis=2)

print 'call member function: \n', a.sum(0)


