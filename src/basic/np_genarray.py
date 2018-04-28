'''
Created on 2017-06-11

@author: btws
'''

import numpy as np

a = np.array([1,2])
print a.shape

b = np.array([ [1,2], [3,4] ])
print b.shape

c = np.array([[[1,2],[3,4]], [[5,6],[7,8]]])
print c.shape

d = np.zeros([3,3])
print d

# the type is object
e = np.array([[1,2],[3,4],[5,6,7]])
print e
print e.shape

# specify data type
f = np.array([1,2,3], dtype=np.int64)
print f
print f.dtype

g = np.array([1,2,3], dtype=np.int32)
print g
print g.dtype

h = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print h.shape, h
h.shape= 2,6
print h
# row, column
h.shape = 6,2
print h
# if col is set to be -1, the size of col would be calculated automatically
h.shape = 3,-1
print h

h.shape= [4,-3]
print h
h.shape=[2,-1]
print h

# not initialize the memory
i = np.empty((4,4), np.int)
print 'i -----'
print i

