from __future__ import print_function

import numpy as np
from scipy.integrate import simps
from numpy import trapz
import sys

def plotfunction ( str ):
        #filename = sys.argv[1]
        nuc = sys.argv[1]
       	half = sys.argv[2]
        filename = '%s/%s/%s_plot.data' % ( nuc, i[j], half )
        #print '%s' % filename
        #data, ydata = np.loadtxt(fname='%s' % filename, delimiter=',', usecols=(0,1), unpack=True)
	xdata, ydata = np.loadtxt(fname='%s' % filename, delimiter=',', usecols=(0,1), unpack=True)
	#Compute the area using the composite trapezoidal rule.
	area = trapz(ydata, dx=0.5)
	print("%s %s %s =" % ( nuc, i[j], half ), area)
	# Compute the area using the composite Simpson's rule.
	#area = simps(ydata, dx=5)
	#print("area =", area)

i=[0, 200, 400, 600, 800, 1000, 1200, 1400]

for j in xrange(0, 8):
        plotfunction(j)
