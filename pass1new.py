import pandas as pd 
import numpy as np 
import math
from astropy import units as u
from astropy.coordinates import SkyCoord
from joblib import Parallel, delayed
import multiprocessing



def filereader(filename):


	df1 = pd.read_csv(filename)
	return df1


def pass1(i,j):


	arr = []
	x = df['X'][i] * df['X'][j]

	y = df['Y'][i] * df['Y'][j]

	z = df['Z'][i] * df['Z'][j]

	tot = x + y + z

	if tot >1: 
		tot = 1

	angle = math.acos(tot)

	arcsec = angle * ((180/math.pi) * 3600)

	'''
	print arcsec
	'''
	print angle,arcsec," i j ", i , j
	
	if arcsec < 5 :
	 	return (i,j)
	else:

		 return None


def filewriter(data_f2,data_f3):

	writename = '~/Data/NonDuplicate.csv'

	data_f2.to_csv(writename,sep=',')	
				
	writename2 = '~/Data/Duplicate.csv'

	data_f3.to_csv(writename2,sep=',')	
	


def data_split(arr):

	'''
	num2 = df.values 

	
	num2 = np.delete(num2,)
	'''

		

	df2 = df

	df3 = df
	#print arr

	df2 = df2.drop([i for i in arr])

	df3 = df3.drop([i for i in xrange(0,len(df)) if i not in arr])
	
	
	return (df2,df3)





if __name__ == "__main__":

	filename = '~/Data/test2.csv'
	
	global df 

	df = filereader(filename)
	
	num_cores = multiprocessing.cpu_count()
	
	results_i  = Parallel(n_jobs=num_cores)(delayed(pass1)(i,j) for i in xrange(0,(len(df)-1)) for j in xrange((i+1),(len(df))))

	#results2 = way2(data_frame1)
	print results_i
	

	results_i = np.unique(results_i)

	print results_i
	results_i =  np.delete(results_i,0)

	liss_i = [ x[0] for x in results_i ]
	liss_i = np.asarray(liss_i)
	liss_j = [ x[1] for x in results_i]
	liss_j = np.asarray(liss_j)
	
	results_i = np.concatenate([liss_i,liss_j])

	
	results_i = np.unique(results_i)
	print results_i
	
	print len(results_i)

	print results_i

	data_frame2 , data_frame3 = data_split(results_i)

	filewriter(data_frame2,data_frame3)

	
	#print results_i
