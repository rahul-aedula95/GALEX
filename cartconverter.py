import pandas as pd 
import numpy as np
from astropy import units as u
from astropy.coordinates import SkyCoord
from joblib import Parallel, delayed
import multiprocessing
#import copy

def filereader(filename):


	df1 = pd.read_csv(filename)
	return df1



def degreetocart(data_f1):
	
	global df2
	df2 = data_f1.copy()
	print "phase 1"

	df2['X'] = np.nan
	df2['Y'] = np.nan
	df2['Z'] = np.nan
	df2 = df2.astype(float)

	print "phase 2"
	num_cores = multiprocessing.cpu_count()
	
	
	results_x = Parallel(n_jobs=num_cores)(delayed(xloop)(i) for i in xrange(0,len(df2)))
	print "phase 3"
	#print results_x

	#print results_x
	
	#print " this is "
	#print results_x[0]

	results_y = Parallel(n_jobs=num_cores)(delayed(yloop)(i) for i in xrange(0,len(df2)))
	print "phase 4"
	results_z = Parallel(n_jobs=num_cores)(delayed(zloop)(i) for i in xrange(0,len(df2)))
	print "phase 5"
	#print results_y



	#Parallel(n_jobs=num_cores)(delayed(adjloop)(i) for i in xrange(0,len(df2)))
	for i in xrange(0,len(df2)):
		print i
		df2['X'][i] = results_x[i]
		df2['Y'][i] = results_y[i]
		df2['Z'][i] = results_z[i]


def xloop(i):
	c = SkyCoord(ra=df2['ra'][i]*u.degree, dec=df2['dec'][i]*u.degree)
	#print i
	val = c.cartesian.x
	return float(val)

def zloop(i):
	c = SkyCoord(ra=df2['ra'][i]*u.degree, dec=df2['dec'][i]*u.degree)
	#print i
	val = c.cartesian.z
	return float(val)


	#print val
	#print df2['mmm'][i]

def yloop(i):
	c = SkyCoord(ra=df2['ra'][i]*u.degree, dec=df2['dec'][i]*u.degree)
	#print i
	val = c.cartesian.y
	return float(val)

def filewriter(data_f2):

	writename = '~/Data/OPTDATA.csv'

	data_f2.to_csv(writename,sep=',')







if __name__ == "__main__":

	filename = '~/Data/OptTable.csv'
	
	data_frame1 = filereader(filename)

	
	degreetocart(data_frame1)
	filewriter(df2)
	#print df2