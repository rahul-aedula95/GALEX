import pandas as pd 
import numpy as np 
import math
from astropy import units as u
from astropy.coordinates import SkyCoord


def filereader(filename):


	df1 = pd.read_csv(filename)
	return df1
x = 0
y = 0
z = 0
def way1(df):


	arr = []


	for i in xrange(0,len(df)):

		for j in xrange((i+1),len(df)):

			x = df['X'][i] * df['X'][j]

			y = df['Y'][i] * df['Y'][j]

			z = df['Z'][i] * df['Z'][j]

			tot = x + y + z

			angle = math.acos(tot)

			arcsec = angle * ((180/math.pi) * 3600)

			print arcsec

		if arcsec > 5 :
			arr.append(i)

	
	return arr			


def way2(df):


	print "######################################################################"

	print "Way 2 "

	print "######################################################################"
	arr = []


	for i in xrange(0,len(df)):

		for j in xrange((i+1),len(df)):

			x = df['X'][i] * df['X'][j]

			y = df['Y'][i] * df['Y'][j]

			z = df['Z'][i] * df['Z'][j]

			tot = x + y + z
			print tot
		if tot > math.cos(0.000024240684055):

			arr.append(i)


	return arr		










if __name__ == "__main__":

	filename = '~/Data/test2.csv'
	
	data_frame1 = filereader(filename)

	results  = way1(data_frame1)

	#results2 = way2(data_frame1)
	
	print results

	print results2

	print math.cos(0.000024240684055)














	