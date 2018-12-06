'''
Created on 2017-08-09

@author: btws
'''

import numpy as np

a = np.array([1,2,3,4], dtype=np.int32)
b = np.array([1,2,3,4], dtype=np.int64)

c = np.array([5,6,7,8], dtype=np.double)

print 'a: \n', a
print 'dtype of a: ', a.dtype

print 'b: \n', b
print 'dtype of b: ', b.dtype

m1 = np.concatenate((a,c))
print 'm1: \n', m1

m2 = np.vstack((a,c))
m3 = np.hstack((a,c))

print 'm2: \n', m2
print 'm3: \n', m3

