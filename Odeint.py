from scipy.integrate import odeint
import pylab as plt


Ro = 2.0
So = 12.0
kr = 0.5
ks = 3.0

Yo = [Ro, So]

def func1(R, t):
    return -kr*R

def func2(Y, t):
    dRdt = -kr*Y[0]
    dSdt = kr*Y[0] - ks*Y[1]
    return [dRdt, dSdt]


T1 = [0,1,2,3,4,5,6,7,8,9,10]
T2 = []

for i in range(21):
    T2 += [i*0.5]







calcDerivada1 = odeint(func1, Ro, T1)
print(calcDerivada1)

plt.plot(T1, calcDerivada1)
plt.show()

print()

calcDerivada2 = odeint(func1, Ro, T2)
print(calcDerivada2)

plt.plot(T2, calcDerivada2)
plt.show()

print()

calcDerivadaDupla = odeint(func2, Yo, T2)
print(calcDerivadaDupla)

plt.plot(T2, calcDerivadaDupla[:,0])
plt.plot(T2, calcDerivadaDupla[:,1])
plt.show()