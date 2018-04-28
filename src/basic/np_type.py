'''
Created on 2017-06-18

@author: btws
'''

import numpy as np

print np.typeDict['int']
print np.typeDict['i']

print np.array([1,2], dtype=np.complex)
# dtype could not be used
print np.array([2,3,4], np.int32)

