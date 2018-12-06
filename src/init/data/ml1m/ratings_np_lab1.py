'''
Created on 2018-10-12

@author: steven
'''


import numpy as np

rating_file_path = 'E:/data/ml_dataset/data/grouplens/ml1m/ratings.dat'

file = open(rating_file_path)
doc = file.read()

lines = doc.split('\n')
data = []

for line in lines:
    if len(line) == 0:
        pass
    else:
        try:
            record = [int(item) for item in line.split('::')]
            data.append(record)
        except:
            print (line)
            pass
matrix = np.mat(data)
ratings = matrix[:,0:3]
m1=ratings[0:3]



