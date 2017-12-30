import itertools
import multiprocessing

#Generate values for each parameter
a = range(1000000)
b = range(1000000)


#Generate a list of tuples where each tuple is a combination of parameters.
#The list will contain all possible combinations of parameters.
paramlist = list(itertools.product(a,b))

print paramlist
#A function which will process a tuple of parameters
def func(params):
  a = params[0]
  print a

  b = params[1]
  print b
  return a*b

#Generate processes equal to the number of cores
pool = multiprocessing.Pool()

#Distribute the parameter sets evenly across the cores
res  = pool.map(func,paramlist)

#print res