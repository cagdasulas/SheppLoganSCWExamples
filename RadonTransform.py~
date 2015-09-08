import math
import numpy as np

import scipy.interpolate
import scipy.misc
import scipy.ndimage.interpolation

def RadonTransform(picture, minTheta=0, maxTheta=180, nProjections=20):

    (pheight,pwidth) = picture.shape
    outP = numpy.zeros(shape = (nProjections, pwidth)
    thetaVector = np.linspace(minTheta, maxTheta, nProjection)

    for index in range(0,nProjections):
        theta = thetaVector[index];
        projectionVector = ProjectionAngle(picture,theta)
        outP[index,:] = projectionVector[0,:];
    return(outP,thetaVector)
    
