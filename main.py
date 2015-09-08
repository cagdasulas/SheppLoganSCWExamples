import math
import numpy as np
import scipy.misc


def main()
  phantom=scipy.misc.imread("Phantom.jpg")
  minAngle=0
  maxAngle=180
  projectionsNumber=5;
  
  # Apply the radon transfrom with the given angles and number of projections
  radonImage=RadonTransform(phantom,minAngle,maxAngle,projectionsNumber) 
  
  # Save the output image
  scipy.misc.imsave("radonTransformedImage",radonImage)