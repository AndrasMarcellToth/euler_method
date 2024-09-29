#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:58:42 2024

@author: andris
"""

import numpy as np
from matplotlib import pyplot as plt
from plotter import Figure

x0 = 0
y0 = 1
h = 0.03
N = 10
n = int(N / h)


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


N = 100000
x_true = np.linspace(0, N, 1000)
y_true = np.sqrt(x_true)

fit_x = np.linspace(0.01, 0.1, 100)


h_list = [0.05, 0.04, 0.03, 0.02, 0.015, 0.01, 0.009, 0.008, 0.007, 0.006, 0.005]
b_list = []

for i in h_list:
    x, y = euler(x0, y0, i, N)
    y_true = np.sqrt(x)
    for j in range(len(x)):
        if abs(y[j] - y_true[j]) > 1:
            print(x[j])
            b_list.append(x[j])
            break
        
fig = Figure(x_label="Step Size (s)", y_label="Breakdown value (s)")
fig.plot(h_list, b_list, c='k')
fig.save("breakdown_value.svg")

