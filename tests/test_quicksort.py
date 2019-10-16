import unittest

from algorithms.quicksort import quicksort, partition_subarray


class TestQuickSort(unittest.TestCase):
    # TODO: find off by one error that's causing test_quicksort to sporadically fail
    def test_quicksort(self):
        # reverse order input
        arr = [5, 4, 3, 2, 1]
        sorted_arr = quicksort(arr)
        assert sorted_arr == [1, 2, 3, 4, 5]

        # already sorted
        arr = [1, 2, 3, 4, 5]
        sorted_arr = quicksort(arr)
        assert sorted_arr == [1, 2, 3, 4, 5]

    def test_partition_subarray(self):
        arr = [3, 1, 2, 4, 5]
        (lt_subarray_bounds, gt_subarray_bounds) = partition_subarray(arr, 0, len(arr) - 1)

        left_subarray = arr[lt_subarray_bounds[0]:lt_subarray_bounds[1] + 1]
        right_subarray = arr[gt_subarray_bounds[0]:gt_subarray_bounds[1] + 1]

        pivot = left_subarray.pop()
        for el in left_subarray:
            assert el < pivot

        for el in right_subarray:
            assert el > pivot
