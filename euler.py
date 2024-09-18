import matplotlib.pyplot as plt
import numpy as np


x0 = 0
y0 = 1
h1 = 0.01
h2 = 0.05
h3 = 0.01
n = 1000
tau = 1


def f(x, y):
    return -y/tau


def ori(x):
    return np.e ** (-x/tau)


def euler(x0, y0, h, n):
    euler_array_x = np.zeros([n+1], dtype='float64')
    euler_array_y = np.zeros([n+1], dtype='float64')
    y = y0
    x = x0
    euler_array_x[0] = x
    euler_array_y[0] = y
    for i in range(1, n+1):
        d = f(x, y)
        y += d * h
        x = x0 + i*h
        euler_array_x[i] = x
        euler_array_y[i] = y
    return euler_array_x, euler_array_y



def rungkutt(x0, y0, h, n):
    rungkutt_array_x = np.zeros([n + 1], dtype='float64')
    rungkutt_array_y = np.zeros([n + 1], dtype='float64')
    y = y0
    x = x0
    rungkutt_array_x[0] = x
    rungkutt_array_y[0] = y
    for i in range(1, n+1):
        d0 = f(x, y)
        d1 = f(x + h/2, y + d0 * h/2)
        d2 = f(x + h/2, y + d1 * h/2)
        d3 = f(x + h, y + d2 * h)
        d = (d0 + 2*d1 + 2*d2 + d3) / 6
        y += d * h
        x = x0 + i*h
        rungkutt_array_x[i] = x
        rungkutt_array_y[i] = y
    return rungkutt_array_x, rungkutt_array_y


ori_x = np.linspace(0, n*h1, n+1)
ori_y = ori(ori_x)
# plt.plot(ori_x, ori_y, '-r')

x1, y1 = euler(x0, y0, h1, n)
x2, y2 = euler(x0, y0, h2, n)
x3, y3 = euler(x0, y0, h3, n)

x = ori_x
y = ori_y - y1

plt.plot(x, y, '-b')

# plt.plot(ori_x, ori_y, '-r')
# plt.plot(x1, y1, '-g')

plt.show()