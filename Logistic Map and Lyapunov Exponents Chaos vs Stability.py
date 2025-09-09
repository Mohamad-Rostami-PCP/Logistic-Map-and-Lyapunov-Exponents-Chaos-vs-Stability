# import libraries
import numpy
import numpy as np
import matplotlib.pyplot as plt
from math import log as log

# Variables
N = 100  # Number of steps

X_1_29 = np.zeros(N)
X_1_365 = np.zeros(N)
X_2_29 = np.zeros(N)
X_2_365 = np.zeros(N)

x_0_1 = 0.1
x_0_2 = 0.101


# The equation function

def Logistic(X, x_0, r):
    size = X.shape[0]

    for n in range(size):
        if n == 0:
            X[n] = x_0
        elif n == (size - 1):
            continue
        X[n + 1] = r * X[n] * (1 - X[n])


# recieving data

# for r = 2.9
Logistic(X_1_29, x_0_1, 2.9)
Logistic(X_2_29, x_0_2, 2.9)

# for r = 3.65
Logistic(X_1_365, x_0_1, 3.65)
Logistic(X_2_365, x_0_2, 3.65)

# delta(x)
delta_X_29 = X_1_29 - X_2_29
delta_X_365 = X_1_365 - X_2_365

# lieponof exponent
Li_29 = numpy.log(numpy.absolute(delta_X_29))
Li_365 = numpy.log(numpy.absolute(delta_X_365))

lambda_29 = Li_29 / (np.arange(N) + 1)
lambda_365 = Li_365 / (np.arange(N) + 1)

# Plotting the data
fig = plt.figure()
fig.set_size_inches(16, 16)
plt.rcParams['font.size'] = '25'
plt.rcParams['lines.linewidth'] = 4

gs = fig.add_gridspec(4, 2, hspace=0, wspace=0)
(ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8) = gs.subplots(sharex='col')
fig.suptitle('\n      r=2.9                                       r=3.65')

ax1.plot(X_1_29, linewidth=3)
ax1.plot(X_2_29, "*", ms=10)
ax1.set(ylabel='x\n\n')
ax1.legend(['x0 = 0.1', 'x0 = 0.101'], loc='lower center')

ax2.plot(X_1_365)
ax2.plot(X_2_365)
ax3.set(ylabel='Δx')

ax3.plot(delta_X_29)

ax4.plot(delta_X_365)

ax5.plot(Li_29)
ax5.set(ylabel='λt\n')
ax6.plot(Li_365)

ax7.plot(lambda_29)
ax7.set(ylabel='λ')
ax7.set_ylim(-1, 0)
ax7.set(xlabel='time (s)')
ax8.plot(lambda_365)
ax8.set_ylim(-1, 0)
ax8.set(xlabel='time (s)')

plt.show()
