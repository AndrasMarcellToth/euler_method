import numpy as np
from matplotlib import pyplot as plt
from plotter import Figure

t0 = 0
x0 = 0
y0 = 1
h = 0.01
N = 100
n = int(N / h)

tau = 1


def f(x, y, t):
    return y

def g(x, y, t):
    return -x

def euler(t0, x0, y0, h, N):
    n = int(N/h)
    t = np.zeros(n+1, 'float64')
    x = np.zeros(n+1, 'float64')
    y = np.zeros(n+1, 'float64')
    
    t[0] = t0
    x[0] = x0
    y[0] = y0
    
    for i in range(1, n+1):
        ti = t[i-1] + h
        xi = x[i-1] + h * f(x[i-1], y[i-1], t[i-1])
        yi = y[i-1] + h * g(x[i-1], y[i-1], t[i-1])
        t[i] = ti
        x[i] = xi
        y[i] = yi

    return t, x, y








fig = Figure(figsize=[5, 5])


t, x, y = euler(t0, x0, y0, h, N)

fig.plot(t, x, m='', ls='-', lw=1)
