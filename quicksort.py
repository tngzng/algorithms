import random

def quicksort(list, left_bound=0, right_bound=None):
    """
    Sorts a list in place by recursively partitioning the list, where the values in the first section of the list are unordered elements less than a randomly selected pivot element and the values in the second section of the list are unordered elements greater than a randomly selected pivot element.

    :param list list: An unordered list containing comparable elements.
    :param int left_bound: Index for left bound of subarray.
    :param int right_bound: Index for right bound of subarray.
    :returns: An ordered list.
    """
    if not right_bound:
        random.shuffle(list) # randomly sort on first call to prevent worst case scenario
        right_bound = len(list) - 1 # right_bound is the last index on the first call

    if right_bound - left_bound < 2:
        return list # done recursing when the subarray has 1 element

    (lt_subarray_bounds, gt_subarray_bounds) = partition(list, left_bound, right_bound)

    quicksort(list, lt_subarray_bounds[0], lt_subarray_bounds[1])
    quicksort(list, gt_subarray_bounds[0], gt_subarray_bounds[1])

    return list

def partition(list, left_bound, right_bound):
    """
    :param list list: An unordered list containing comparable elements.
    :param int left_bound: Index for left bound of subarray.
    :param int right_bound: Index for right bound of subarray.
    :returns: A tuple of tuples -- the left and right bounds for the elements smaller than the pivot and the left and right bounds for the elements larger than the pivot.
    """
    pivot = list[left_bound]
    # TODO more descriptive var names for i and j
    # i is the partition between the less than and greater than sides
    # j is the partition for unchecked portion
    i = left_bound + 1
    for j in range(left_bound + 1, right_bound + 1):
        if list[j] < pivot:
            # swap list[j] and list[i] bc list[j] belongs with smaller els
            temp = list[j]
            list[j] = list[i]
            list[i] = temp
            i += 1
    # swap pivot at list[left_bound] and list[i - 1], the last of the smaller than pivot els
    temp = list[left_bound]
    list[left_bound] = list[i - 1]
    list[i - 1] = temp

    return ((left_bound, i - 1), (i, right_bound))

list = [ 1, 2, 9, 5, 4, 6, 7, 3, 0, 100, -100, 10000 ]
print quicksort(list)







