#Sherry Wong
#15 August 2022

#This file requires .txt files from Carrie's plotting code.

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

### USER SETUP
#ipopt .dat --> plotting code .txt
pred = np.loadtxt('Mary_3beam_regular/P1z_IC1_beta28.txt')
#forward integration output
fwdinteg = np.loadtxt('Mary_3beam_regular/P1zA_.txt')
#Xi file - real fwdintegurement/data
meas = np.loadtxt('Mary_3beam_regular/Xi1_.txt')

### INTERPOLATE
#num steps to average
chunk = 3000

N = len(pred)   # length of original .txt file: 121901
stop = int(N - chunk - 1)

#Mean for ipopt data
i = 0
predMean = []
while i < stop:
    j = int(i+chunk)
    m = np.mean(pred[i:j])
    predMean.append(m)
    i += chunk

#Mean for forward integration data
i = 0
fwdintegMean = []
while i < stop:
    j = int(i+chunk)
    m = np.mean(fwdinteg[i:j])
    fwdintegMean.append(m)
    i += chunk


### compare final results
#last mean prediction vs. measurement
print('measured:\t\t\t' + str(meas[-1]))
print('mean:\t\t\t\t' + str(predMean[-1]))
print('difference(mean-measured):\t' + str(predMean[-1]-meas[-1]))
#last mean prediction vs. last mean fwd integration
print()
print('forward integration:\t\t' + str(fwdinteg[-1]))
print('mean:\t\t\t\t' + str(predMean[-1]))
print('difference(mean-fwd):\t\t' + str(predMean[-1]-fwdinteg[-1]))

### PLOT ipopt and fwd integration
fig = plt.figure(figsize=(8,8))
orig_r = np.linspace(0, len(pred), len(pred))
r = np.arange(len(predMean))*chunk #adjusted to match original domain
#original outputs
plt.plot(orig_r, fwdinteg, color='blue', label='fwd integ')
plt.plot(orig_r, pred, color='black', label='prediction', alpha=0.5)
#smooth mean curve
plt.plot(r, fwdintegMean, color='blue', lw=5, ls=':', label='expected mean')
plt.plot(r, predMean, color='purple', lw=5, label='predicted mean')
#labels + asthetics
plt.ylabel('$\\nu_e$ flavor')
plt.xlabel('x position')
plt.legend()
fig.savefig("Means")
plt.close()
