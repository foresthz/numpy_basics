'''
Created on 2017-06-28

@author: btws
'''

import numpy as np
from numpy.random import randn, standard_normal, normal

# randn is shortcut of standard_normal

m1 = randn(3,3)
print 'matrix m1\n:', m1

m2 = standard_normal([4,4])
print 'matrix m2\n:', m2

m3 = standard_normal((2,3))
print 'matrix m3:\n', m3

m4 = randn(6,5)*9 + 11
print 'matrix m4:\n', m4

n1 = normal(10,100,(3,3))
print '\nnormal matrix n1:\n', n1
