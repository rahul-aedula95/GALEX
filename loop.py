import pandas as pd 
import numpy as np 
import math

from joblib import Parallel, delayed
import multiprocessing
'''
a=0
for i in xrange(0,1600000):
	for j in xrange(0,1600000):
		a=(a+1)/1
		print j
'''

num_cores = multiprocessing.cpu_count()
print num_cores
'''
def loop(i):

	print i		


results_i  = Parallel(n_jobs=num_cores, backend="multiprocessing")(delayed(loop)(i) for i in xrange(0,1600000)) #xrange((i+1)	
'''
'''
filename = '~/Data/DATA2.csv'

df1 = pd.read_csv(filename)

for i in xrange(0,2):
	for j in xrange(i+1,len(df1)):
		print j
		arr = []
		x = df1['X'][i] * df1['X'][j]

		y = df1['Y'][i] * df1['Y'][j]

		z = df1['Z'][i] * df1['Z'][j]

		tot = x + y + z

		if tot >1: 
			tot = 1

		angle = math.acos(tot)

		arcsec = angle * ((180/math.pi) * 3600)

		if arcsec < 5:
			arr.append(i)

print len(arr)
'''