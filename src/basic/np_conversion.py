'''
Created on 2017-06-19

@author: btws
'''

import numpy as np

a = np.arange(0,20,2)
a1 = a.tolist()
print 'type of a: ', type(a)
print 'type of a1: ', type(a1)

b = np.arange(2,22,2)
c = b.reshape(2,5)
d = np.copy(b)
print b[0], c[0][0], d[0]
b[0]=100
print 'b and c point to different memory region, the only difference is that they have different axis'
print b[0], c[0][0], d[0]

