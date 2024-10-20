import math

import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint

import books_ref


class Example:
    def __init__(self, book: books_ref.Book, page: str):
        self.book = book
        self.page = page
        self.model = None
        self.ic = None, None # t0, values: list
        self.solution = None

    def get_ic_t(self):
        return self.ic[0]
    def get_ic_y(self):
        return self.ic[1]

# function that returns dy/dt
def model10(y, t, k):
    dydt = y * y * t * t / (1 + t * t)
    return dydt

example1 = Example(books_ref.books['Alan'], '244')
example1.model = model10
example1.ic = 0, [1]


def solution1(x):
    return 1/(math.atan(x) - x + 1)

def calc(example, t_stop):
    t = np.linspace(example.get_ic_t(), t_stop)
    sol1 = [solution1(x) for x in t]

    # solve ODEs
    k = 1 #fictious parameter
    y1 = odeint(example1.model,example.get_ic_y(),t,args=(k,))
    #
    abs_err = [math.fabs(sol1[i] - y1[i][0]) for i in range(0, len(t))]
    return {
        't': t,
        'sol': y1,
        'ref': sol1,
        'abs_err': abs_err,
    }

t_stop = 1
res = calc(example1, 1)
#
def show_result(solution, x_axis, y_axis, title_solution, ref_solution):
    t = solution['t']
    y1 = solution['sol']
    ref = solution['ref']
    abs_err = solution['abs_err']
    fig, ax1 = plt.subplots()
    #
    ax1.plot(t,y1,'g-',linewidth=2,label=f'{title_solution}')
    ax1.plot(t,ref,'b--',linewidth=2,label=f'{ref_solution}')
    plt.xlabel(x_axis)
    ax1.set_ylabel(y_axis)
    ax1.legend()
    #
    ax2 = ax1.twinx()  # instantiate a second Axes that shares the same x-axis
    color = 'tab:red'
    ax2.set_ylabel('abs_error', color=color)  # we already handled the x-label with ax1
    #
    ax2.plot(t, abs_err, color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    #
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()

x_axis = 'time'
y_axis = 'y(t)'
title_solution = "Num.solution"
ref_solution = "Ref.solution"
show_result(res, x_axis, y_axis, title_solution, ref_solution)