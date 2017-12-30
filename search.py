import numpy as np 
import pandas as pd 

filename = '~/Data/DataSet.csv'

df1 = pd.read_csv(filename)

x = df1.values

count = 0
row,col = np.shape(x)

for i in xrange(0,row):
	if x[i][1] == x[0][7] :

		count = count + 1


print "the row is"
print row
print "the count is"
print count 		