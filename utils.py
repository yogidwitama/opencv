import numpy as np
import cv2

def get_limits(color):
    # Create a BGR color array with the correct data type
    c = np.uint8([[color]])
    
    # Convert BGR color to HSV
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    
    # Define lower and upper HSV limits
    lowerLimit = (hsvC[0][0][0] - 10, 100, 100)
    upperLimit = (hsvC[0][0][0] + 10, 255, 255)
    
    # Convert limits to numpy arrays of uint8
    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)
    
    return lowerLimit, upperLimit
