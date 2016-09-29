import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '../..'))
import unittest
from get_ith_largest import partition, get_ith_largest


class TestGetIthLargest(unittest.TestCase):
    def test_partitions(self):
        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        (partitioned_arr, pivot_location) = partition(arr)

        pivot = partitioned_arr[pivot_location]
        for el in partitioned_arr[:pivot_location]:
            assert el < pivot

        for el in partitioned_arr[pivot_location:]:
            assert el >= pivot

    def test_get_ith_largest(self):
        # unordered list
        arr = [5, 4, 3, 2, 1]
        ith_largest = get_ith_largest(arr, 5)
        assert ith_largest == 5

        # ordered list
        arr = [1, 2, 3, 4, 5]
        ith_largest = get_ith_largest(arr, 5)
        assert ith_largest == 5
