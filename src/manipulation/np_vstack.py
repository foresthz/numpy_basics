'''
Created on 2017-07-31

@author: btws
'''

import numpy as np

t1 = np.arange(0,9,1)
t2 = np.arange(10,19,1)

t3 = np.arange(11,15,1)
t4 = np.arange(100,112,1)

t5 = np.arange(200,206,1)
t6 = np.arange(300,303,1)

a = t1.reshape(3,3)
b = t2.reshape(3,3)
c = t3.reshape(2,2)

d = t4.reshape(4,3)
e = t5.reshape(3,2)
f = t6.reshape(3,1)


m1 = np.vstack((a,b))

m2 = np.vstack((a,d))

print 'a: \n', a
print 'b: \n', b
print 'm1:\n', m1

# cannot concatenate b and c

print 'm2: \n', m2

'''very powerful vstack'''

m3 = np.vstack((a,d))

m4 = np.vstack((d,a))

print 'a d > m3 \n', m3
print 'd a > m4 \n', m4


