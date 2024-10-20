import math
import unittest

from examples import examples
from uget import uget
from util_calc import calc


class AddTest(unittest.TestCase):
    def test_1(self):
        example = examples['example1']
        res = calc(example)
        t_last = uget(res, ['t', -1])
        y_last = uget(res, ['sol', -1])
        assert math.fabs(y_last[0] - examples['example1'].sol_ref.func(t_last)) < 1e-4
        pass

if __name__ == '__main__':
    unittest.main()
