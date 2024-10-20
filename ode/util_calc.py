import math

import numpy as np
from scipy.integrate import odeint

from ode import books_ref
from ode.uget import uget


class Model:
    def __init__(self, t0: float, y_init: list, f_func):
        self.t0 = t0
        self.y_init = y_init
        self.f_func = f_func

class Book_Ref:
    def __init__(self, book: books_ref.Book, page: str):
        self.book = book
        self.page = page

    def __str__(self):
        return f"{self.book}, p.{self.page}"


class Solution_Ref:
    def __init__(self, book_ref: Book_Ref, func, t_stop: float):
        self.book_ref = book_ref
        self.func = func
        self.t_stop = t_stop


class Example:
    def __init__(self, book_ref: Book_Ref, model: Model, sol_ref: Solution_Ref):
        self.book_ref = book_ref
        self.model = model
        self.sol_ref = sol_ref


def calc(example, t_stop=None):
    t = np.linspace(example.model.t0, t_stop if t_stop is not None else example.sol_ref.t_stop)
    ref_sol = [example.sol_ref.func(x) for x in t]

    # solve ODEs
    k = 1 #fictious parameter
    pack = (k,)
    y1 = odeint(example.model.f_func, example.model.y_init, t, args=pack)
    #
    abs_err = [math.fabs(ref_sol[i] - uget(y1, [i, 0])) for i in range(0, len(t))]
    return {
        't': t,
        'sol': y1,
        'ref': ref_sol,
        'abs_err': abs_err,
        'example': example,
    }
