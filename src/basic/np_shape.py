'''
Created on 2017-06-09

@author: btws
'''

import numpy as np

from scipy.misc import face
face=face()
print face.shape

a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print a.shape
print a
# the matrix is changed
a.shape=(3,4)
print a.shape
print a

# reshape does not change the axis of matrix
print a.reshape(4,3)
print a

a = np.zeros([3,4])
b = np.zeros((4,3))

print a
print b
print b.reshape([2,6])
print b.reshape((6,2))

# -1 can be used in any place.
c = np.arange(0,27,1)
print 'shape of c: ', c.shape
d = c.reshape([3,3,3])
print 'shape of d: ', d.shape
e = c.reshape([3,3,-1])
print 'shape of e: ', e.shape
f= c.reshape([-1,3,3])
print 'shape of f: ', f.shape

