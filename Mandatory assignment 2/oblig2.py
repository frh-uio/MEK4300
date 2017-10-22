import numpy as np
import matplotlib.pyplot as pyplot
from math import sqrt, log

N=1000000
Re_L = np.linspace(0, 1E6, N)

C_D = np.zeros(N)
C_D[0] = 0

C_D_B = np.zeros(N)
C_D_B[0] = 0

for i in range(1,len(Re_L)):
	C_D[i] = 1.3101/sqrt(Re_L[i])

pyplot.figure()
pyplot.loglog(Re_L, C_D)
pyplot.xlabel('$Re_L$')
pyplot.ylabel('$Drag \quad Coefficient \quad C_D(L)$')
pyplot.show()
