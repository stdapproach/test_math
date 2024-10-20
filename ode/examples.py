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

examples = {
    'example1': Example(ref1, model1, sol_ref1)
}
