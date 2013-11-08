#define a function to find the closest grid point to some desired location X, Y

import os
import netCDF4 as NC
import numpy as np

def find_closest_model_point(lon,lat,X,Y,bathy):
	#find the closest model grid point to the measured data

	#tolerance for searching for grid points (approx. distances between adjacent grid points)
	tol1 = 0.0052  #lon
	tol2 = 0.00189 #lat
    
	#search for a grid point with lon/lat within tolerance of measured location 
	x1, y1=np.where(np.logical_and((np.logical_and(X>lon-tol1,X<lon+tol1)),np.logical_and(Y>lat-tol2,Y<lat+tol2)))
	if np.size(x1)!=0:
		x1 = x1[0]
        	y1 = y1[0]
        #What if more than one point is returned from this search? Just take the first one...
	
		#if x1,y1 is masked, search 3x3 grid around. If all those points are masked, search 4x4 grid around etc
		for ii in np.arange(1,100):
		    if bathy.mask[x1,y1]==True:
		        for i in np.arange(x1-ii,x1+ii+1):
		            for j in np.arange(y1-ii,y1+ii+1):
		                if bathy.mask[i,j] == False:		
		                    break
		            if bathy.mask[i,j] == False:
		                break
		        if bathy.mask[i,j] == False:
		            break
		    else:
		        i = x1
		        j = y1
	else:
        	i=[]
        	j=[]
    	return i, j