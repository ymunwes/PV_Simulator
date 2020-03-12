# Python code for 1-D random walk. 
import random 
import numpy as np 
import matplotlib.pyplot as plt 
import time


class randomWalk():
    def __init__(self, initVal=0, probDown=0.5, probUp=0.5, resolution=100, lowerLimit=0.0, upperLimit=9000.):
        self._initVal = initVal
        self._probDown = probDown
        self._probUp = probUp
        self._resolution = resolution
        self._lowerLimit = lowerLimit
        self._upperLimit = upperLimit
        
    def __del__(self):
        print('Destructor called')
        
    def getVal(self, currentPower):
        rnd = np.random.random()
        downp = rnd < self._probDown
        upp = rnd > self._probUp
        down = (downp and currentPower > self._lowerLimit) * self._resolution
        up = (upp and currentPower < self._upperLimit) * self._resolution
        if currentPower - down + up >= 0:
            return currentPower - down + up
        else:
            return 0
        

        
