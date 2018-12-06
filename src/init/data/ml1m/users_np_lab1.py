'''
Created on 2018-09-27

@author: steven
'''

import re

ml1m_user_file_path = 'E:/data/ml_dataset/data/grouplens/ml1m/users.dat'

file = open(ml1m_user_file_path)

doc = file.read()

lines = doc.split('\n')

def parse_line(line):
    arr = line.split('::')
    
    m = re.match('\d+$', arr[4])
    if m is None:
        arr[4] = '00000'
        
    if(arr[1] == 'F'):
        arr[1] = '0'
    else:
        arr[1] = '1'
    return [int(x) for x in arr]

data = []
for line in lines:
    if len(line) == 0:
        pass
    else:
        record = parse_line(line)
        data.append(record)

