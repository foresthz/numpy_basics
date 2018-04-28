'''
Created on 2017-06-18

@author: btws
'''

import numpy as np

a = np.arange(0,1,0.1)
print a

# the last digit stands for number of splits
b = np.linspace(0,1,6)
print b, 'size of b: ', len(b)

# the default base is 10, from 10^0 to 10^2
c = np.logspace(0,2,5)
print c
d = np.logspace(0,10,12, base=2)
print d


