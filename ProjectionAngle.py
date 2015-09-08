import math

import numpy as np

import scipy.interpolate

import scipy.misc

import scipy.ndimage.interporalation

def ProjectionAngle(Image, Angle)

	rotatedImage=scipy.ndimage.interporalation.rotate(Image,Angle,order=3,reshape=False,
	                                                        mode='constant', cval=0.0)
															
    imageSum=np.sum(rotatedImage,axis=0)
	
	return imageSum