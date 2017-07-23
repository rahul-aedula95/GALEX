import pandas as pd
from astropy.io import fits
import numpy as np
import os
import glob
def ListReader(file_name):
	lis = []
	with open(file_name) as fp:

		for line in fp:
			if not line.isspace():
				lis.append(line.rstrip())
	fp.close()	
	return lis

def FileLister(dir_name):

	flist = []

	for filename in glob.glob(os.path.join(dir_name, '*.fits')):

		flist.append(filename)

	return flist	

def FileReader(file_list,param_list):

	row_add = np.zeros(shape=(1,len(param_list)+1))

	for file in file_list:
		hdulist = fits.open(file,memmap=True)
		data_in = hdulist[1].data
		col_add = np.zeros(shape=(len(data_in),1))
		print file
		for param in param_list:
			data_now = np.reshape(data_in[param],(len(data_in[param]),1))
			col_add = np.append(col_add,data_now,axis=1)

		row_add = np.append(row_add,col_add,axis=0)	
		del hdulist

	
	row_add = np.delete(row_add,0,axis=0)
	row_add = np.delete(row_add,0,axis=1)	
	return row_add	


def DataToCSV(concat_data,param_list,write_name):

	df1 = pd.DataFrame(data=concat_data,columns=param_list)

	df1.to_csv(write_name, sep=',')





if __name__ == "__main__":

	dir_name = '/home/astro/Data'
	
	file_name = 'ParsedParameters.txt'

	write_name = '/home/astro/Data/DataSet.csv'

	param_list = ListReader(file_name)

	file_list = FileLister(dir_name)
	
	concat_data = FileReader(file_list,param_list)

	DataToCSV(concat_data,param_list,write_name)
	
	