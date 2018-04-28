'''
Created on 2017-08-09

@author: btws
'''

import numpy as np

a = np.array([1,2,3,4])

print 'a: \n', a
print 'shape of a: \n', a.shape

a.shape=(4,1)
print 'after envaluate (4,1) to a.shape, a: \n', a

a.shape=4
print 'let a.shape be 4, a:\n', a
print 'a.shape : ', a.shape

# it can be the same as (2,2)
a.shape = [2,2] 
print a

# no need to use parenthesis when using reshape
a.shape = 1,4
print 'when shape is 1,4 : \n', a
a.shape = 4
print 'when shape is 4: \n', a