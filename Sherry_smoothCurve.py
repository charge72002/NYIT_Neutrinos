#Sherry Wong
#11 August 2022

#This file requires .txt files from Carrie's plotting code.

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#ipopt .dat --> plotting code .txt
pred = np.loadtxt('P1z_IC1_beta30.txt')
#forward integration output
meas = np.loadtxt('P1zA_.txt')

### INTERPOLATE
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
measMean = []
while i < stop:
    j = int(i+chunk)
    m = np.mean(meas[i:j])
    measMean.append(m)
    i += chunk


#compare final results
print('measured:\t\t\t' + str(measMean[-1]))
print('mean:\t\t\t\t' + str(predMean[-1]))
print('difference(mean-measured):\t' + str(predMean[-1]-measMean[-1]))

### PLOT
fig = plt.figure(figsize=(8,8))
orig_r = np.linspace(0, len(pred), len(pred))
r = np.arange(len(predMean))*chunk #adjusted to match original domain
plt.plot(orig_r, meas, color='blue', label='fwd integ')
plt.plot(orig_r, pred, color='black', label='prediction', alpha=0.5)
plt.plot(r, measMean, color='blue', lw=5, ls=':', label='expected mean')
plt.plot(r, predMean, color='purple', lw=5, label='predicted mean')
plt.ylabel('$\\nu_e$ flavor')
plt.xlabel('x position')
plt.legend()
fig.savefig("Means")
plt.close()
