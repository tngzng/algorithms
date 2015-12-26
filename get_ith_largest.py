import random

def get_ith_largest(arr, i):
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

def partition(arr):
    # select random el to use as pivot and move to start of arr
    rand_int = random.randint(0, len(arr) - 1)
    temp = arr[0]
    arr[0] = pivot = arr[rand_int]
    arr[rand_int] = temp

    boundary = 1 # initalize boundary bw smaller and greater els as first unsorted
    for next_unsorted in range(1, len(arr)):
        if arr[next_unsorted] < pivot:
            # move next_unsorted with the smaller els
            temp = arr[next_unsorted]
            arr[next_unsorted] = arr[boundary]
            arr[boundary] = temp
            boundary += 1

    # swap pivot and the last of the smaller els
    new_pivot_location = boundary - 1
    temp = arr[0] # old pivot location
    arr[0] = arr[new_pivot_location]
    arr[new_pivot_location] = temp

    return (arr, new_pivot_location)

arr = [ 1, 2, 9, 5, 4, 6, 7, 3, 0, 100, -100, 10000 ]
print get_ith_largest(arr, 11) # expect 100
