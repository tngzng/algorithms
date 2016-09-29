import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '../..'))
import unittest
from count_inversions import count_inversions, merge_and_count_inversions

class TestCountInversions(unittest.TestCase):
    def test_merge_and_count_inversions(self):
        # no inversions
        a = [1]
        b = [2]
        res = merge_and_count_inversions(a, b)
        assert res['list'] == [1, 2]
        assert res['count'] == 0

        # one inversion
        a = [2]
        b = [1]
        res = merge_and_count_inversions(a, b)
        assert res['list'] == [1, 2]
        assert res['count'] == 1

        # multiple else left in a when el from b appended to merged list
        a = [2, 3]
        b = [1]
        res = merge_and_count_inversions(a, b)
        assert res['list'] == [1, 2, 3]
        assert res['count'] == 2

    def test_count_inversions(self):
        # no inversions
        list = [0, 1, 2, 3, 4]
        res = count_inversions(list)
        assert res['count'] == 0

        # list in reverse order has (n - 1)! inversions
        list = [4, 3, 2, 1, 0]
        res = count_inversions(list)
        assert res['count'] == 4 + 3 + 2 + 1
