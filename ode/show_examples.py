from examples import examples
from uget import uget
from util_calc import calc
from util_chart import show_result


def show_custom(key: str):
    res = calc(uget(examples, [key]))
    x_axis = 'time'
    y_axis = 'y(t)'
    title_solution = "Numerical.solution"
    ref_solution = "Ref.solution"
    show_result(res, x_axis, y_axis, title_solution, ref_solution)

#show_custom('example2')
#show_custom('example3')
#show_custom('example4')
#show_custom('example5')
#show_custom('example6')
#show_custom('example7')
show_custom('example8')
