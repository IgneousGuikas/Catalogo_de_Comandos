from scipy.integrate import odeint
import pylab as plt


Ro = 2.0
k = -0.5

def func1(k, Ro):
    return k*Ro

T1 = [0,1,2,3,4,5,6,7,8,9,10]
T2 = []

for i in range(21):
    T2 += [i*0.5]

calcDerivada1 = odeint(func1, Ro, T1)
print(calcDerivada1)

plt.plot(T1, calcDerivada1)
plt.show()