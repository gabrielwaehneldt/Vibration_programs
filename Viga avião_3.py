import numpy as np
from math import sin
from scipy.linalg import eigh
from numpy.linalg import inv
from matplotlib import pyplot as plt

# setup the parameters
F0 = 15791.0
omega = 628
k = 158848
mt = 629.6
ne = 4
m=mt/ne #massa do elemento
L=8 #comprimento da barra
l=L/ne #comprimento elemento
time_step = 1.0e-4
end_time = 10.0

# setup matrices
K=np.zeros([ne,ne])

for i in range(ne):
    if i==0:
        K[i,i]=2*k
        K[i,i+1]=-k
    if i==(ne-1):
        K[i,i]=2*k
        K[i,i-1]=-k
    if i!=0 and i!=(ne-1):
        K[i,i-1]=-k
        K[i,i]=2*k
        K[i,i+1]=-k
    

M=np.zeros([ne,ne])
for i in range(ne):
    M[i,i]=m*(1/3)*(l)**2

I = np.identity(ne)

A = np.zeros((2*ne,2*ne))
B = np.zeros((2*ne,2*ne))
Y = np.zeros((2*ne,1))
F = np.zeros((2*ne,1))

A[0:ne,0:ne] = M
A[ne:2*ne,ne:ne*2] = I

B[0:ne,ne:2*ne] = K
B[ne:ne*2,0:ne] = -I

# find natural frequencies and mode shapes
evals, evecs = eigh(K,M)
frequencies = np.sqrt(evals)
print ("frequencias: " +str(frequencies))
print (evecs)

A_inv = inv(A)
force = []
X1 = []
X2 = []
X3 = []
X4 = []
# numerically integrate the EOMs
for t in np.arange(0, end_time, time_step):
	F[1] = F0 * sin(omega*t)
	Y_new = Y + time_step * A_inv.dot( F - B.dot(Y) )
	Y = Y_new
	force.extend(F[1])
	X1.extend(Y[3])
	X2.extend(Y[4])
	X3.extend(Y[5])
	X4.extend(Y[6])

# plot results
time = [round(t,5) for t in np.arange(0, end_time, time_step) ]

plt.plot(time,X1)
plt.plot(time,X2)
plt.plot(time,X3)
plt.plot(time,X4)

plt.xlabel('time (s)')
plt.ylabel('displacement (m)')
plt.title('Response Curves')
plt.legend(['X1', 'X2', 'X3', "X4"], loc='lower right')
plt.show()

#plt.plot(time,force)
#plt.show()
