'''
Created on 2017-06-26

@author: btws
'''

from numpy.random import random, random_sample

import numpy as np

# random is alias for random_samples, the default range is [0,1) 

a = random(10)
print 'matrix a (1x10) : \n', a

# sum and np.sum can both be used to sum list, the latter can be used to sum up matrix
print 'sum of ndarray', sum(a), np.sum(a)

b = random((3,3))
print 'matrix b: \n', b

c = random_sample((2,2))

