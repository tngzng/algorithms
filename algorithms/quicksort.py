from typing import List, Optional, Tuple
import random


def quicksort(arr: List[int], left_bound: int = 0, right_bound: Optional[int] =None) -> list:
    """
    Sorts a list in place by recursively partitioning the list. Each partition orders a smaller subarray and produces new subarrays to partition.

    :param arr list: An unordered list containing integers.
    :param int left_bound: Index for left bound of subarray.
    :param int right_bound: Index for right bound of subarray.
    :returns: An ordered list.
    """
    initial_call = right_bound == None
    if initial_call:
        random.shuffle(arr) # prevent worst case scenario
        right_bound = len(arr) - 1

    if right_bound - left_bound < 2:
        return arr # done recursing when the subarray has 1 element

    (lt_subarray_bounds, gt_subarray_bounds) = partition_subarray(arr, left_bound, right_bound)

    quicksort(arr, lt_subarray_bounds[0], lt_subarray_bounds[1])
    quicksort(arr, gt_subarray_bounds[0], gt_subarray_bounds[1])

    return arr


def partition_subarray(arr: List[int], left_bound: int, right_bound: int) -> Tuple[Tuple[int, int]]:
    """
    Partition a subarray into two subarrays, one with values less than a pivot and one with values greater than a pivot. The subbarray is also ordered by swapping elements when out of place in relation to the pivot.

    :param arr list: An unordered list containing integers.
    :param int left_bound: Index for left bound of subarray.
    :param int right_bound: Index for right bound of subarray.
    :returns: A tuple of tuples representing new bounds for each new partition.
    """
    pivot = arr[left_bound]
    new_bound = left_bound + 1
    for next_unsorted in range(new_bound, right_bound + 1):
        if arr[next_unsorted] < pivot:
            # move next_unsorted with the smaller els
            temp = arr[next_unsorted]
            arr[next_unsorted] = arr[new_bound]
            arr[new_bound] = temp
            new_bound += 1
    # swap pivot and the last of the smaller els
    temp = arr[left_bound] # pivot location
    arr[left_bound] = arr[new_bound - 1]
    arr[new_bound - 1] = temp

    return (left_bound, new_bound - 1), (new_bound, right_bound)
