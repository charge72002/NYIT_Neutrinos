import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import os

#%matplotlib inline

### USER MANUALLY ENTERS THE FOLLOWING: ###
Date = '2021dec16'
n_states = int(10) # Number of variables (for neutrinos model: P1x,P1y,P1z,P2x,P2y,P2z,,P3x,P3y,P3z,r (We have to manually include dr/dr=1.)
n_controlVariables = int(0)
n_statesAndControls = int(n_states + n_controlVariables)
n_meas = int(7) # N measurements.  
n_params = int(0) # Number of unknown parameters.
n_beams = 3 # Number of beams

skip_data = 0 # How much data you skipped
problem_length = 121901  # How many discretized points in the problem (specs.txt length)*2 + 1
dt = 2.85237 # discretized step size  (specs.txt / 2)
###########################################

IC = 1  # Initial path to plot
ICmax = 5  # Max on path to plot (i.e. if ICmax=4, then the final path plotted will be IC3.) 

betaMax = 30  # This must be initialized, but its value will be changed - once we read in a file - to that file length.

while IC < ICmax:  # Loop over all paths
    beta = 0
    while beta < betaMax:  # For each path, Loop over beta
        infile = int(IC)

        file_name = ('D%s_M%s_IC%s.dat' % (n_states, n_meas, infile))
        time_series = np.loadtxt(file_name)
        betaMax = len(time_series)
        
        print('IC:', IC, ', beta:', beta, ', betaMax:', betaMax)

        '''Define new outfolders:'''
        directory = ('IC%s/' % IC)
        if not os.path.exists(directory):
            os.makedirs(directory)
        else: print('huffalumps')
        
        completed_annealing_steps =  beta #len(time_series[:,0])
        #Gets the path for the last annealing step in ipopt file (beta=30 or
        #something like that)
        last_anneal_step_time_series = time_series[completed_annealing_steps - 1, :]

        #The value of the action at that annealing step
        action_level = last_anneal_step_time_series[beta]

        if n_params > 0: 
            print('n params is greater than 0:', n_params)
            my_time_series = last_anneal_step_time_series[3:-n_params]
        else: 
            print('n params is 0:', n_params)
            my_time_series = last_anneal_step_time_series[3:]
            
#        '''IF n params > 0:'''
#        my_time_series = last_anneal_step_time_series[3:-n_params]
#        
#        '''IF n params = 0:'''
#        my_time_series = last_anneal_step_time_series[3:]

        print('shape of my Ipopt output before reshaping:', my_time_series.shape)
        
        #reshapes for analysis. Format is (-1,number_of_states)
        my_time_series = my_time_series.reshape((-1,n_statesAndControls))

        print('shape of my Ipopt output:', my_time_series.shape)

        #name of your simulation file goes here
        true_data = []
        for n in range(n_beams):
            true_data.append(np.loadtxt('P%sz_.txt' % (n+1)))
        #true_data = np.loadtxt('P1z_.txt')
        #true_data2 = np.loadtxt('P2z_.txt')
        #true_data3 = np.loadtxt('P3z_.txt')
        injectedVmatt = np.loadtxt('Vmatt_.txt')

        true_y = true_data#[:,1]   ## the y values are the 1st row of sim.txt.
#        true_P2 = true_data[:,2]  
#        true_P3 = true_data[:,3]
#        true_P5 = true_data[:,5]  
#        true_P6 = true_data[:,6]
#        true_time = true_data[:,7]

        true_y = true_y[skip_data:skip_data + problem_length]
        injectedVmatt = injectedVmatt[skip_data:skip_data+problem_length]
#        true_P1 = true_P1[skip_data:skip_data + problem_length]
#        true_P2 = true_P2[skip_data:skip_data + problem_length]
#        true_P3 = true_P3[skip_data:skip_data + problem_length]
#        true_P4 = true_P4[skip_data:skip_data + problem_length]
#        true_P5 = true_P5[skip_data:skip_data + problem_length]
#        true_P6 = true_P6[skip_data:skip_data + problem_length]
#        true_time = true_time[skip_data:skip_data + problem_length]
##        true_Cm = true_Cm[skip_data:skip_data + problem_length]

        for n in range(n_beams):
            np.savetxt('%s/P%sz_IC%s_beta%s.txt' % (directory, n+1, IC, beta), my_time_series[:,n*3+2])
        #np.savetxt('%s/y_IC%s_beta%s.txt' % (directory, IC, beta), my_time_series[:,0])  # Save Ipopt solution to .txt
#        np.savetxt('%s/P1x_IC%s_beta%s.txt' % (directory, IC, beta), my_time_series[:,0])  # Save Ipopt solution to .txt
#        np.savetxt('%s/P1y_IC%s_beta%s.txt' % (directory, IC, beta), my_time_series[:,1])
#        np.savetxt('%s/P1z_IC%s_beta%s.txt' % (directory, IC, beta), my_time_series[:,2])
#        np.savetxt('%s/P2x_IC%s_beta%s.txt' % (directory, IC, beta), my_time_series[:,3])
#        np.savetxt('%s/P2y_IC%s_beta%s.txt' % (directory, IC, beta), my_time_series[:,4])
#        np.savetxt('%s/P2z_IC%s_beta%s.txt' % (directory, IC, beta), my_time_series[:,5])
#        np.savetxt('%s/r_IC%s_beta%s.txt' % (directory, IC, beta), my_time_series[:,6])
#        np.savetxt('%s/Cm_IC%s_beta%s.txt' % (directory, IC, beta), my_time_series[:,7])
                
        #Create the time array
        time = np.linspace(skip_data*dt, (skip_data + problem_length)*dt,
        (problem_length))

        alpha = 0.7   # Set opacity so that we can compare model to prediction regardless of which one is plotted first.

        ymin, ymax = -1, 3.
        
        FONT = 14
        
        for n in range(n_beams):
            fig = plt.figure(figsize=(8,8))
            plt.subplot(1,1,1)
            plt.plot(time, true_y[n], color = 'b', label = 'model P%sz' % (n+1),alpha=alpha,linestyle='dotted')
            plt.plot(time, my_time_series[:,n*3+2], color = 'k', label = 'predicted P%sz' % (n+1),alpha=alpha)
            #plt.plot(time, injectedVmatt, color='r', label = 'Vmatt',alpha=alpha)
            plt.ylim((ymin,ymax))
            #plt.ylabel(r'$P_{1z}$',fontsize='xx-large')
    #        plt.xticks(ticks=[], labels=[])
            plt.legend(loc='upper right', fontsize='x-large')
            plt.show()
            fig.savefig('%s/TSeries_all_IC%s_beta%s_edit_P%sz' % (directory, IC, beta, n+1))
            plt.close()
        
        fig1 = plt.figure(figsize=(8,8))
        plt.plot(time, injectedVmatt, color='r', label = 'model Vmatt',alpha=alpha)
        plt.legend(loc='upper right', fontsize='x-large')
        fig1.savefig('%s/Vmatt_IC%s_beta%s_edit' % (directory, IC, beta))
        plt.close()
        
#         fig0 = plt.figure(figsize=(8,8))
#         plt.subplot(1,1,1)
#         plt.plot(time, true_y, color = 'b', label = 'model P1z',alpha=alpha,linestyle='dotted')
#         plt.plot(time, my_time_series[:,2], color = 'k', label = 'predicted P1z',alpha=alpha)
#         #plt.plot(time, injectedVmatt, color='r', label = 'Vmatt',alpha=alpha)
#         plt.ylim((ymin,ymax))
#         #plt.ylabel(r'$P_{1z}$',fontsize='xx-large')
# #        plt.xticks(ticks=[], labels=[])
#         plt.legend(loc='upper right', fontsize='x-large')
#         plt.show()
#         fig0.savefig('%s/TSeries_all_IC%s_beta%s_edit' % (directory, IC, beta))
#         plt.close()        
#         fig1 = plt.figure(figsize=(8,8))
#         plt.plot(time, injectedVmatt, color='r', label = 'model Vmatt',alpha=alpha)
#         plt.legend(loc='upper right', fontsize='x-large')
#         fig1.savefig('%s/Vmatt_IC%s_beta%s_edit' % (directory, IC, beta))
#         plt.close()
        
#         fig2 = plt.figure(figsize=(8,8))
#         plt.subplot(1,1,1)
#         plt.plot(time, true_data2, color = 'b', label = 'model P2z',alpha=alpha,linestyle='dotted')
#         plt.plot(time, my_time_series[:,5], color = 'k', label = 'predicted P2z',alpha=alpha)
#         #plt.plot(time, injectedVmatt, color='r', label = 'Vmatt',alpha=alpha)
#         plt.ylim((ymin,ymax))
#         #plt.ylabel(r'$P_{1z}$',fontsize='xx-large')
# #        plt.xticks(ticks=[], labels=[])
#         plt.legend(loc='upper right', fontsize='x-large')
#         plt.show()
#         fig2.savefig('%s/TSeries_all_IC%s_beta%s_edit_P2' % (directory, IC, beta))
#         plt.close()
        
#         fig3 = plt.figure(figsize=(8,8))
#         plt.subplot(1,1,1)
#         plt.plot(time, true_data3, color = 'b', label = 'model P3z',alpha=alpha,linestyle='dotted')
#         plt.plot(time, my_time_series[:,8], color = 'k', label = 'predicted P3z',alpha=alpha)
#         #plt.plot(time, injectedVmatt, color='r', label = 'Vmatt',alpha=alpha)
#         plt.ylim((ymin,ymax))
#         #plt.ylabel(r'$P_{1z}$',fontsize='xx-large')
# #        plt.xticks(ticks=[], labels=[])
#         plt.legend(loc='upper right', fontsize='x-large')
#         plt.show()
#         fig3.savefig('%s/TSeries_all_IC%s_beta%s_edit_P3' % (directory, IC, beta))
#         plt.close()
        
        beta += 1
    IC += 1
