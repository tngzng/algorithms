import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '../..'))
import unittest
from merge_sort import merge, merge_sort


class TestMergeSort(unittest.TestCase):
    def test_merge(self):
        # a is exhausted first
        a = [1, 2]
        b = [3, 4]
        merged_arr = merge(a, b)
        assert merged_arr == [1, 2, 3, 4]

        # b is exhausted first
        a = [3, 4]
        b = [1, 2]
        merged_arr = merge(a, b)
        assert merged_arr == [1, 2, 3, 4]

    def test_merge_sort(self):
        # reverse order input
        arr = [5, 4, 3, 2, 1]
        sorted_arr = merge_sort(arr)
        assert sorted_arr == [1, 2, 3, 4, 5]

        # already sorted
        arr = [1, 2, 3, 4, 5]
        sorted_arr = merge_sort(arr)
        assert sorted_arr == [1, 2, 3, 4, 5]
