import math
import unittest

from examples import examples
from uget import uget
from util_calc import calc


class AddTest(unittest.TestCase):
    def test_1(self):
        key = 'example1'
        example = examples[key]
        res = calc(example)
        t_last = uget(res, ['t', -1])
        y_last = uget(res, ['sol', -1])
        assert math.fabs(y_last[0] - examples[key].sol_ref.func(t_last)) < 1e-4
        pass

    def test_2(self):
        key = 'example2'
        example = examples[key]
        res = calc(example)
        t_last = uget(res, ['t', -1])
        y_last = uget(res, ['sol', -1])
        assert math.fabs(y_last[0] - examples[key].sol_ref.func(t_last)) < 1e-4
        pass

    def test_3(self):
        key = 'example3'
        example = examples[key]
        res = calc(example)
        t_last = uget(res, ['t', -1])
        y_last = uget(res, ['sol', -1])
        assert math.fabs(y_last[0] - examples[key].sol_ref.func(t_last)) < 1e-4
        pass

    def test_4(self):
        key = 'example4'
        example = examples[key]
        res = calc(example)
        t_last = uget(res, ['t', -1])
        y_last = uget(res, ['sol', -1])
        assert math.fabs(y_last[0] - examples[key].sol_ref.func(t_last)) < 1e-4
        pass

    def test_5(self):
        key = 'example5'
        example = examples[key]
        res = calc(example)
        t_last = uget(res, ['t', -1])
        y_last = uget(res, ['sol', -1])
        assert math.fabs(y_last[0] - examples[key].sol_ref.func(t_last)) < 1e-4
        pass

    def test_6(self):
        key = 'example6'
        example = examples[key]
        res = calc(example)
        t_last = uget(res, ['t', -1])
        y_last = uget(res, ['sol', -1])
        assert math.fabs(y_last[0] - examples[key].sol_ref.func(t_last)) < 1e-4
        pass

if __name__ == '__main__':
    unittest.main()
