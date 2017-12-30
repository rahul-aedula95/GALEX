import pandas as pd
filename = '~/Data/OptTable.csv'

df1 = pd.read_csv(filename)
count = 0
for i in xrange(0,len(df1)):

	if df1['dec'][i] < 28.138707 and df1['dec'][i] > 28.1381523: 
		count = count +1


print count	