import numpy as np
from matplotlib import pyplot as plt
from plotter import Figure

x0 = 0
y0 = 10
h = 0.1
N = 10
n = int(N / h)

tau = 1


def f(x, y):
    return -y / tau

def ori(x):
    return y0 * np.e ** (-x / tau)

def euler(x0, y0, h, N):
    n = int(N/h)
    x = np.zeros(n+1, 'float64')
    y = np.zeros(n+1, 'float64')
    
    x[0] = x0
    y[0] = y0
    
    for i in range(1, n+1):
        xi = x[i-1] + h
        yi = y[i-1] + h * f(x[i-1], y[i-1])
        x[i] = xi
        y[i] = yi

    return x, y



x, y = euler(x0, y0, h, N)
yp = ori(x)

yerr = yp - y

fig = Figure()
# fig.plot(x, yp, m='', ls='--', c='k', lw=1)
# fig.plot(x, y, m='', ls='-', lw=1)
fig.line(x, yerr)





