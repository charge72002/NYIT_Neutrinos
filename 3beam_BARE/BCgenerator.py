# -*- coding: utf-8 -*-
"""
Created on Sat May 21 17:17:23 2022

@author: carrie
"""

import numpy as np

steps = 121901

BC1andF = np.zeros(steps)
BC1andF[0]=1
BC1andF[-1]=1

BC1only = np.zeros(steps)
BC1only[0]=1

BCFonly = np.zeros(steps)
BCFonly[-1]=1

np.savetxt("BC1andF.txt",BC1andF)
np.savetxt("BC1only.txt",BC1only)
np.savetxt("BCFonly.txt",BCFonly)

#Xis
Xilist=[0,0,-0.22,0,0,-0.26,0,0,-0.30]
for i in range(len(Xilist)):
    Xis = np.zeros(steps)
    Xis[-1] = Xilist[i]
    np.savetxt("Xi%s_.txt" % (i+1),Xis)
