import numpy as np
from matplotlib import pyplot as plt
from plotter import Figure

t0 = 0
x0 = 0
y0 = 1
h = 0.1
N = 5
n = int(N / h)

tau = 1


def f(x, y, t):
    return y

def g(x, y, t):
    return -x

def ori(t):
    return np.sin(t)

def euler(t0, x0, y0, h, N):
    n = int(N/h)
    t = np.zeros(n+1, 'float64')
    x = np.zeros(n+1, 'float64')
    y = np.zeros(n+1, 'float64')
    
    t[0] = t0
    x[0] = x0
    y[0] = y0
    
    for i in range(1, n+1):
        
        cx1 = h * f(x[i-1],  y[i-1], t[i-1])
        cy1 = h * g(x[i-1],  y[i-1], t[i-1])
        cx2 = h * f(x[i-1] + cx1, y[i-1] + cy1, t[i-1] + h)
        cy2 = h * g(x[i-1] + cx1, y[i-1] + cy1, t[i-1] + h)
        xi = x[i-1] + 0.5 * (cx1 + cx2)
        yi = y[i-1] + 0.5 * (cy1 + cy2)
        ti = t[i-1] + h
        t[i] = ti
        x[i] = xi
        y[i] = yi

    return t, x, y

t, x, y = euler(t0, x0, y0, h, N)
xori = ori(t)

fig = Figure(figsize=[5, 5])

fig.plot(t, x, m='', ls='-', lw=1)
fig.plot(t, y, m='', ls='-', lw=1, c='r')