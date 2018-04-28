'''
Created on 2017-06-11

@author: btws
'''

import numpy as np

def arithmic_function():
    a = np.array([1, 2, 3])
    b = np.array((1,2,3))
    c = np.array([3,4,3])
    print 'a:', a
    print 'b:', b
    print 'c:', c
    # compare one by one
    print 'a==b:', a == b
    print 'a==c:', a == c
    # add one by one
    print 'a+b:', a+b
    
    # error
    #print np.sum([1,2],[2,3])
    # can output the right answer
    print np.sum([[1,2],[2,3]])
    print np.sum(([1,2],[2,3]))
    
    # concat
    print np.sum([[1,2,3,4],[1,2],[5,5]])
    print np.sum(np.sum([[1,2,3,4],[1,2],[5,5]]))
    
def change_shape():
    a = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12]])
    print a