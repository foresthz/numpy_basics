'''
Created on 2017-06-19

@author: btws
'''

import numpy as np
from numpy.random import uniform

a = np.arange(0,10,1)

print 'a'
print a
b = a.reshape([2,5])

c = np.arange(11,22,1,np.long)

d = np.zeros([3,3])
e = np.zeros([3,3], np.int)

f = uniform(10, size=(3,3))
g = uniform(15,33, size=(2,2))

h = np.ones([3,3], np.float)
i = np.ones((2,2), np.int32)
j = np.ones([3,3], dtype=np.double)

print 'b:'
print b
print '----------------'
print 'b transpose:'
print b.T

print 'memory layout of matrix a: '
print a.flags

print '----- dimensions:'
print 'dim of a:', a.ndim
print 'dim of b:', b.ndim

print '----- strides:'

print '----- number of elements :'
print 'size of a: ', a.size
print 'size of b: ', b.size

print '----- how many bytes one element occupies, itemsize:'
print 'itemsize of a, b: ', a.itemsize, b.itemsize
print 'itemsize of c: ', c.itemsize
print 'the defulat itemsize of zeros() is long: ', d.itemsize
print 'specify type for zeros(), now the itemsize is: ', e.itemsize

print '----- total bytes of array: '
print a.nbytes , a.itemsize, a.size

print '----- base of b: '
print 'a:'
print a
print 'b'
print b

# original layout
print 'base of a: '
print a.base
# b is reshaped from a
print 'base of b: '
print b.base

print 'when a is changed, b is also changed, because they point to the same region in memory.'
a[0]=100
print a
print b

print '\nrandom initialize: '
print 'matrix f: \n', f
print 'matrix g: \n', g

print '\ninit with type ...'
print 'matrix h of type float: \n', h
print 'matrix i of type integer: \n', i
print 'matrix j with type parameter: \n', j



