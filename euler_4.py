import numpy as np
from matplotlib import pyplot as plt
from plotter import Figure

t0 = 0
x0 = 0
y0 = 1
h = 0.1
N = 30
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
        ti = t[i-1] + h
        xi = x[i-1] + h * f(x[i-1], y[i-1], t[i-1])
        yi = y[i-1] + h * g(x[i-1], y[i-1], t[i-1])
        t[i] = ti
        x[i] = xi
        y[i] = yi

    return t, x, y

def euler_mod(t0, x0, y0, h, N):
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

# t, x, y = euler(t0, x0, y0, h, N)
# tmod, xmod, ymod = euler_mod(t0, x0, y0, h, N)
# xori = ori(t)

# fig = Figure(x_min=0, x_max=N, x_label="Time (s)", y_label="Displacement (m)")

# fig.plot(t, x, m='', ls='-', lw=0.7, label="Euler Approximation")
# fig.plot(tmod, xmod, m='', ls='-', lw=0.7, label="Modified Euler Approximation")
# fig.plot(t, xori, m='', ls='--', c='k', lw='0.7', label="Exact Solution")

# fig.legend()



font = {'family': 'serif', 'size': 10, 'color': 'black'}
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8), dpi=600)

# Set the common x-axis label
ax2.set_xlabel('Time (s)', fontdict=font)

# Set the y-axis labels for each plot
ax1.set_ylabel('Displacement (m)', fontdict=font)
ax2.set_ylabel('Error (m)', fontdict=font)
plt.subplots_adjust(hspace=0)
ax1.set_xlim([0, N])
ax2.set_xlim([0, N])
# Set tick parameters without gridlines
for ax in [ax1, ax2]:
    ax.tick_params(which='both', direction='in', labelsize=10)
    ax.minorticks_on()  # Enable minor ticks

ax1.set_xticklabels([])
t, x, y = euler(t0, x0, y0, h, N)
tmod, xmod, ymod = euler_mod(t0, x0, y0, h, N)
xori = ori(t)
xerr = xori - x
xmoderr = xori - xmod


ax1.plot(t, x, marker='', ls='-', lw=0.7, label="Euler Approximation")
ax1.plot(tmod, xmod, marker='', ls='-', lw=0.7, label="Modified Euler Approximation")
ax1.plot(t, xori, marker='', ls='--', lw=0.7, c='k', label="Exact Solution")
ax2.plot(t, xerr, marker='', ls='-', lw=0.7)
ax2.plot(t, xmoderr, marker='', ls='-', lw=0.7)




fig.legend(loc='upper center', bbox_to_anchor=(0.3, 0.87), ncol=1)

# plt.savefig("e4_mod_vs_normal.svg")





























