'''
Created on 2017-06-26

@author: btws
'''

import numpy as np

'''
    randint: closed range, [l, h], if high is not present, the interval should be [0,low], 
    rand_integers: half-open interval, [low,high) , if high is None, the interval should be [1,low) // deprecated 1.10
'''

from numpy.random import randint
from numpy.random import random_integers

a = randint(10, size=[3,3])
print 'matrix a: \n', a

b = randint(22,100, size=(4,4))
print 'matrix b: \n', b

c = randint(101,150,size=[3,4])
print 'matrix c: \n', c

d = randint(3,19,size=[3,3,3])
print 'matrix d: \n', d

# the default parameter is high
e = randint(30, size=[4,6])
print 'matrix e: \n', e

f = randint(-10,10,(10,10))
print 'matrix f: \n', f


