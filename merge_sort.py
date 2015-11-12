def merge_sort(list):
  """
  recursively sorts halved lists, merging the results at each level

  input: unordered list containing comparable elements
  output: ordered list
  """
  if len(list) < 2:
    return list
  mid_point = len(list) / 2
  # recursively sort 1st half of input
  first_half = merge_sort(list[0:mid_point])
  # recursively sort 2nd half of input
  second_half = merge_sort(list[mid_point:len(list)])
  # merge
  return merge(first_half, second_half)

def merge(a, b):
  """
  steps through indexes in both input lists, appending the smaller val at each step

  input: two ordered lists
  output: one ordered list combining the two input lists
  """
  i = 0
  j = 0
  total_len = len(a) + len(b)
  res = []
  for k in range(total_len):
    try:
      a[i]
    except IndexError:
      # concat res w remainder of b if a's finished
      res = res + b[j:len(b)]
      j += 1
      return res

    try:
      b[j]
    except IndexError:
      # concat res w remainder of a if b's finished
      res = res + a[i:len(a)]
      i += 1
      return res

    if a[i] < b[j]:
      res.append(a[i])
      i += 1
    else:
      res.append(b[j])
      j += 1

  return res

list = [ 1, 2, 9, 5, 4, 6, 7, 3, 0, 100, -100, 10000 ]
print merge_sort(list)