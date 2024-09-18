import numpy as np
from matplotlib import pyplot as plt
from plotter import Figure

x0 = 0
y0 = 1
h = 0.05
N = 440
n = int(N / h)

tau = 1


def f(x, y):
    return x - y**2

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








fig = Figure(x_min=435, x_max=N)

for i in np.linspace(5, -0.725, 1):
    x, y = euler(x0, i, h, N)
    fig.plot(x, y, m='', ls='-', lw=0.1)


