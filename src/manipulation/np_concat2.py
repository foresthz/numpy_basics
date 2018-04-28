'''
Created on 2017-08-09

@author: btws
'''

import numpy as np

a = np.array([[1,2], [3,4]])
b = np.array([5,6])

b.shape = 2,1

c = np.array([[7,8]])

# when axis=1, similar as hstack
m1 = np.concatenate((a,b), axis=1)
print 'm1 : \n', m1

m2 = np.hstack((a,b))
print 'm2 : \n', m2

