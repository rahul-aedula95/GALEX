from astropy.io import fits
import numpy as np
hdulist = fits.open('/home/astro/Downloads/GI1_065001_SubaruDeep_21452/GI1_065001_SubaruDeep_0153-xd-mcat.fits')

scidata = hdulist[1].data

print np.shape(scidata)




