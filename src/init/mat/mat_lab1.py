'''
Created on 2018-04-28

@author: jack
'''

import numpy as np

# the least dimension is 2

m0 = np.mat([3,4])
print 'dim of m0: \n', m0.ndim
print 'm0[0]: \n', m0[0]

# only one number means get row of matrix
print 'm0[0][0]: \n', m0[0][0]
print 'm0[0][0][0]: \n', m0[0][0][0]
print 'm0[0,1]: \n', m0[0,1]

print '-----'

m1 = np.mat([[1,2],[3,4]])
print 'm1: \n', m1

print 'm1[0]: \n', m1[0]
