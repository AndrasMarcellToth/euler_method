import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from scipy.special import stdtrit
from scipy.stats import tstd
from tabulate import tabulate



class Figure:
    def __init__(self,
                 subplots = None,
                 figsize=[5.5, 3.999],
                 dpi=600,  # Resolution of image.
                 plot_left=0.125,  # Position of plot in figure.
                 plot_bottom=0.125,  # (0 is all the way to the left/bottom, 1 is all the way to the right/top)
                 plot_right=0.9,
                 plot_top=0.9,
                 **kwargs
                 ):
        if subplots is None:
            self.fig = plt.figure(dpi=dpi, figsize=figsize)
            self.fig.subplots_adjust(left=plot_left, bottom=plot_bottom, right=plot_right, top=plot_top)
            self.ax = self.fig.add_subplot(1, 1, 1)
            self.ax_settings(self.ax, **kwargs)
        else:
            self.fig = plt.figure(dpi=dpi, figsize=figsize)
            self.fig.subplots_adjust(left=plot_left, bottom=plot_bottom, right=plot_right, top=plot_top)

            self.subplots(subplots)

    
    def subplots(self,
                 dimensions):
                
        rows = dimensions[0]
        cols = dimensions[1]
        self.ax = []
        for i in range(1, (rows * cols) + 1):
            ax = self.fig.add_subplot(rows, cols, i)
            self.ax_settings(ax)
            self.ax.append(ax)
        self.fig.tight_layout(pad=0.3)
        return self.ax
    
    def ax_settings(self,
                    ax,
                    x_label='',  # Labels of x and y-axis.
                    y_label='',
                    x_min=None,
                    x_max=None,
                    y_min=None,
                    y_max=None,
                    font=None,  # Font must be passed as a font dict.
                    axes_width=0.5,  # Line width of axes
                    tick_label_size=7,  # Font size of tick mark labels.
                    grid=None,  # Turns on gridlines. Takes 'x', 'y' or 'both'.
                    grid_line_width=0.5,
                    grid_color='grey',
                    sci_lim_upper=10**3,
                    sci_lim_lower=10**-3,
                    box=True,
                    **kwargs
                    ):
        
        if box == False:
            ax.spines['right'].set_visible(False)
            ax.spines['top'].set_visible(False)
        else:
            ax.spines['right'].set_linewidth(axes_width)
            ax.spines['top'].set_linewidth(axes_width)
        ax.spines['left'].set_linewidth(axes_width)
        ax.spines['bottom'].set_linewidth(axes_width)
        ax.set_axisbelow(True)  # Move axes and grid to background.

        ax.minorticks_on()  # Add minor ticks and set tick parameters
        ax.tick_params(axis='both', which='major', direction='in', length=5, width=axes_width,
                            labelsize=tick_label_size)
        ax.tick_params(axis='both', which='minor', direction='in', length=3, width=axes_width)
        ax.ticklabel_format(axis='both', style='sci', useMathText=True)
        if x_min is not None and x_max is not None:
            ax.set_xlim([x_min, x_max])
        if y_min is not None and y_max is not None:
            ax.set_ylim([y_min, y_max])
        if font is None:  # Set font for axes labels.
            font = {'family': 'serif', 'size': 10, 'color': 'black'}
        ax.set_xlabel(x_label, fontdict=font)
        ax.set_ylabel(y_label, fontdict=font)

        if grid == 'both':  # Turn on grid lines.
            ax.grid(axis='x', lw=grid_line_width, c=grid_color)
            ax.grid(axis='y', lw=grid_line_width, c=grid_color)
        elif grid == 'x':
            ax.grid(axis='x', lw=grid_line_width, c=grid_color)
        elif grid == 'y':
            ax.grid(axis='y', lw=grid_line_width, c=grid_color)
            
            
            
fig = Figure(subplots=[2, 1])
