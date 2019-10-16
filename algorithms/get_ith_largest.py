from typing import Tuple
import random


def get_ith_largest(arr: list, i: int) -> int:
    """
    Get the ith largest element of a list by recursively partitioning the list and continuing to search
    in the half of the list where the ith largest element resides.

    :param list arr: A list containing comparable elements.
    :param int i: Represents the order statistic we are looking for.
    :returns: The ith largest el of a list.
    """
    if len(arr) == 1:
        return arr[0]

    (arr, new_pivot_location) = partition(arr)

    if new_pivot_location + 1 == i:
        return arr[new_pivot_location]

    if new_pivot_location + 1 > i:
        new_arr = arr[:new_pivot_location]
        return get_ith_largest(new_arr, i)

    if new_pivot_location + 1 < i:
        new_arr = arr[new_pivot_location:]
        new_i = i - new_pivot_location
        return get_ith_largest(new_arr, new_i)


def partition(arr: list) -> Tuple[list, int]:
    """
    Partition a list by swapping elements when out of place in relation to a randomly selected pivot.

    :param list arr: A list containing comparable elements.
    :returns: A tuple containing the partitioned list and the index of a randomly selected pivot
    (it's correct index in the list).
    """
    # select random el to use as pivot and move to start of arr
    rand_int = random.randint(0, len(arr) - 1)
    temp = arr[0]
    arr[0] = pivot = arr[rand_int]
    arr[rand_int] = temp

    boundary = 1  # initalize boundary bw smaller and greater els as first unsorted
    for next_unsorted in range(1, len(arr)):
        if arr[next_unsorted] < pivot:
            # move next_unsorted with the smaller els
            temp = arr[next_unsorted]
            arr[next_unsorted] = arr[boundary]
            arr[boundary] = temp
            boundary += 1

    # swap pivot and the last of the smaller els
    new_pivot_location = boundary - 1
    temp = arr[0]  # old pivot location
    arr[0] = arr[new_pivot_location]
    arr[new_pivot_location] = temp

    return arr, new_pivot_location
