import numpy as np

#array structure - [value,+stat,-stat,+syst,-syst,+D/N,-D/N]
a0 = [0.0325,0.0366,-0.0360,0.0059,-0.0092,0.0145,-0.0148]
a1 = [-0.0311,0.0279,0.0292,0.0104,-0.0056,0.0140,-0.0129]
c0 = [0.3435,0.0205,-0.0197,0.0111,-0.0066,0.0050,-0.0059]
c1 = [0.00795,0.00780,-0.00745,0.00308,-0.00335,0.00236,-0.00240]
c2 = [-0.00206,0.00302,-0.00311,0.00148,-0.00128,0.00057,-0.00074]

energies = [8.5,9,9.5,10,10.5,11,11.5,12]

def Psurvival(E_nu):
    return c0[0]+c1[0]*(E_nu-10)+c2[0]*(E_nu-10)**2

Psurvivals = []

for E in energies:
    Psurv = Psurvival(E)
    Psurvivals.append(Psurv)
    print("For beam w/ energy %s MeV, P_surv=%s" % (E,Psurv))
    
def findError(E_nu):
    errors=[]
    for errori in range(1,7):
        errors.append(np.sqrt(c0[errori]**2+(E_nu-10)**2*c1[errori]**2+(E_nu-10)**4*c2[errori]**2))
    return errors

for E in energies:
    errors = findError(E)
    print("For beam w/ energy %s MeV, errors=%s" % (E,errors))
    totalPosVar = 0
    totalNegVar = 0
    for errori in range(len(errors)):
        if errori%2==0:
            totalPosVar+=errors[errori]**2
        else:
            totalNegVar+=errors[errori]**2
    print("For beam w/ energy %s MeV, total positive error=%s" % (E,np.sqrt(totalPosVar)))
    print("For beam w/ energy %s MeV, total negative error=%s" % (E,np.sqrt(totalNegVar)))