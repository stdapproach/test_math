import math

import books_ref
from util_calc import Model, Book_Ref, Solution_Ref, Example


# function that returns dy/dt
def d_model10(y, t, k):
    dydt = y * y * t * t / (1 + t * t)
    return dydt

model1 = Model(0, [1], d_model10)
ref1 = Book_Ref(books_ref.books['Alan'], '244')
sol_ref1 = Solution_Ref(ref1, lambda x: 1/(math.atan(x) - x + 1), 1)
#
def d_model20(y, t, k):
    dydt = math.tan(t) - y/math.cos(t)
    return dydt
model2 = Model(0, [2], d_model20)
ref2 = Book_Ref(books_ref.books['Alan'], '256')
sol_ref2 = Solution_Ref(ref2, lambda x: 1+ (1-x)*math.cos(x)/(1+math.sin(x)), 1)

def d_model30(y, t, k):
    dydt = [y[1], -4*y[0]]
    return dydt
model3 = Model(math.pi/4, [1, 1], d_model30)
ref3 = Book_Ref(books_ref.books['Alan'], '274')
sol_ref3 = Solution_Ref(ref3, lambda x: math.sin(2*x)-0.5*math.cos(2*x), math.pi/4+1)
#
def d_model40(y, t, k):
    dydt = [y[1], 2*y[0]-y[1]]
    return dydt
model4 = Model(0, [1, 2], d_model40)
ref4 = Book_Ref(books_ref.books['Alan'], '276')
sol_ref4 = Solution_Ref(ref4, lambda x: (4/3)*math.exp(x) - (1/3)*math.exp(-2*x), 2)

def d_model50(y, t, k):
    dydt = [y[1], -4*y[0]-2*y[1]]
    return dydt
model5 = Model(0, [2, 1], d_model50)
sol_ref5 = Solution_Ref(ref4, lambda x: math.exp(-x)*(math.sqrt(3)*math.sin(x*math.sqrt(3))+2*math.cos(x*math.sqrt(3))), 2)

def d_model60(y, t, k):
    dydt = [y[1], -4*y[0]-4*y[1]]
    return dydt
model6 = Model(0, [3, 1], d_model60)
sol_ref6 = Solution_Ref(ref4, lambda x: math.exp(-2*x)*(3+7*x), 2)

def d_model70(y, t, k):
    dydt = [y[1], -(37/4)*y[0]-(4/4)*y[1]+(12/4)*math.cos(t)]
    return dydt
model7 = Model(0, [1, -2], d_model70)
ref7 = Book_Ref(books_ref.books['Alan'], '288')
def ref70_steady(t):
    return (1/1105)*(48*math.sin(t)+396*math.cos(t))
def ref70_transient(t):
    return (1/2210)*math.exp(-t/2)*(1418*math.cos(3*t)-1269*math.sin(3*t))
sol_ref7 = Solution_Ref(ref7, lambda x: ref70_transient(x) + ref70_steady(x), 20)

def d_model80(y, t, k):
    dydt = [y[1], y[2], -6*y[0]+5*y[1]+2*y[2]]
    return dydt
model8 = Model(0, [1, 0, 0], d_model80)
ref8 = Book_Ref(books_ref.books['Alan'], '300')
sol_ref8 = Solution_Ref(ref8, lambda x: math.exp(x)+(1/5)*math.exp(-2*x)-(1/5)*math.exp(3*x), 2)


examples = {
    'example1': Example(ref1, model1, sol_ref1),
    'example2': Example(ref2, model2, sol_ref2),
    'example3': Example(ref3, model3, sol_ref3),
    'example4': Example(ref4, model4, sol_ref4),
    'example5': Example(ref4, model5, sol_ref5),
    'example6': Example(ref4, model6, sol_ref6),
    'example7': Example(ref7, model7, sol_ref7),
    'example8': Example(ref8, model8, sol_ref8),
}
