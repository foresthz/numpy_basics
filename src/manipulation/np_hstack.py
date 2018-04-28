'''
Created on 2017-07-31

@author: btws
'''

import numpy as np

t1 = np.arange(9)
a = t1.reshape(3,3)

t2 = np.arange(10,19,1)
b = t2.reshape(3,3)

c=np.array([9,8,10])

m1 = np.hstack((a,b))