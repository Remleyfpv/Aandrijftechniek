# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 17:12:11 2024

@author: flint
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import math



maxSlope = 20

F_zh = np.zeros(maxSlope*2)
F_rw = np.zeros(maxSlope*2)
Dload = 0
Sload = np.zeros(maxSlope*2)

slope = np.array(range(-maxSlope,maxSlope,1))

for i in range(maxSlope*2):
    F_zh[i] = 6*1.62*math.sin(math.radians(slope[i])) 
    F_rw[i] = 0.1*6*1.62*math.cos(math.radians((slope[i])))
    Sload[i] = ((F_zh[i] + F_rw[i])*0.075)/4
    
    
plt.plot(slope,Sload)
plt.show()
