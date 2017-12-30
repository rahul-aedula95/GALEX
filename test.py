import pandas as pd
import matplotlib.pyplot as pl
from astropy.io import fits
import numpy as np
from matplotlib.colors import LogNorm
hdulist = fits.open('/home/astro/Data/GI1_065001_SubaruDeep_0153-xd-mcat.fits')

hdulist.info()

scidata = hdulist[1].data


'''
sci = np.reshape(scidata['ggoid_hex'],(len(scidata['ggoid_hex']),1))

#print sci
sci2 = np.reshape(scidata['ggoid_dec'],(len(scidata['ggoid_dec']),1))

sci3 = np.append(sci,sci2,axis=1)
 
cols  = ['A','B']

df1 = pd.DataFrame(data=sci3,columns=cols)

#df1 = df1['A'].append(sci)

print df1

'''
'''
fields = ['ggoid_hex','ggoid_dec']

for f in fields:
	print scidata[f]

'''

print scidata['ggoid']





