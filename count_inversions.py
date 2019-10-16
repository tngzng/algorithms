def count_inversions(list: list, inversion_count: int = 0) -> dict:
    """
    recursively counts inversions of halved lists
    where inversions are instances where a larger el occurs before a smaller el
    merges the halved lists and increments the inversion count at each level

    :param list list: list containing comparable elements
    :param list list: list containing comparable elements
    :returns: {'list': the ordered list, 'count': total number of inversions}
    """
    if len(list) < 2:
        return { "list": list, "count": inversion_count }
    mid_point = len(list) // 2

    # recursively count inversions in 1st half of input
    first_half = count_inversions(list[0:mid_point], inversion_count)
    # recursively count inversions in 2nd half of input
    second_half = count_inversions(list[mid_point:len(list)], inversion_count)

    running_inversion_count = first_half["count"] + second_half["count"]
    return merge_and_count_inversions(first_half["list"], second_half["list"], running_inversion_count)


def merge_and_count_inversions(a: list, b: list, inversion_count: int = 0) -> dict:
    """
    steps through indexes in both input lists, appending the smaller val to the merged list at each step
    increments the inversion count when els from list b are appended to the output before a is exhausted

    :param list a: ordered list
    :param list b: ordered list
    :returns: {'list': the ordered list, 'count': total number of inversions}
    """
    i = 0
    j = 0
    total_len = len(a) + len(b)
    merged = []
    for k in range(total_len):
        try:
            a[i]
        except IndexError:
            # concat merged w remainder of b if a's finished
            merged = merged + b[j:len(b)]
            j += 1
            return { "list": merged, "count": inversion_count }

        try:
            b[j]
        except IndexError:
            # concat merged w remainder of a if b's finished
            merged = merged + a[i:len(a)]
            i += 1
            return { "list": merged, "count": inversion_count }

        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
            # increment inversion_count by num els remaining in a if a isn't exhausted
            try:
                a[i]
                remaining_in_a = len(a) - i
                inversion_count = inversion_count + remaining_in_a
            except IndexError:
                pass # a is exhausted

    return { "list": merged, "count": inversion_count }
