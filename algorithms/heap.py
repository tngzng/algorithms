from typing import List, Optional


class Heap:
    """
    This is a heap implementation that uses an array. Since a heap is an as-complete-as-possible binary tree,
    the parent and children of any given key in the heap can be found by simple arithmetic.
    For example, let's say we have the following heap:
             1
            / \
           2   3
          / \
         4   5

    We can represent the heap as the array:
    [1, 2, 3, 4, 5]

    The parent of key 5 can be found by taken the floor of the key's position divided by 2.
    5 // 2 = 2

    Similarly, the children of key 2 can be found by multiplying the key's position and adding 1.
    2 * 2 = 4
    2 * 2 + 1 = 5
    """
    def __init__(self) -> None:
        self.heap: List[int] = []

    def insert(self, key: int) -> None:
        """
        Accepts a key and places it in a position that maintains the integrity of the heap.
        (ie in a position where the key is greater than its parent.)
        """
        self.heap.append(key)
        position = len(self.heap)
        self.bubble_up(key, position)

    def bubble_up(self, key: int, position: int) -> None:
        """
        Recursively swaps the input child key with its parent, until it is greater than or equal to its parent.
        """
        parent_position = self.parent_position(position)
        if not parent_position:
            return
        parent = self.heap[parent_position - 1]
        if parent and parent > key:
            self.swap(position, parent_position)
            position = parent_position
            self.bubble_up(key, position)

    def extract_min(self) -> int:
        """
        Returns the minimum key from the heap and reorders the remaining keys to maintain the integrity of
        the heap, so that any given child is less than it's parent.
        """
        res = self.heap[0]
        self.heap[0] = self.heap.pop()
        position = 1
        key = self.heap[position - 1]
        self.bubble_down(key, position)
        return res

    def bubble_down(self, key: int, position: int) -> None:
        """
        Recursively swaps the inputted parent key with it's minimum child, until it is less than or
        equal to its minimum child.
        """
        min_child_pos = self.min_child_position(position)
        if not min_child_pos:
            return
        min_child = self.heap[min_child_pos - 1]
        if key > min_child:
            self.swap(position, min_child_pos)
            position = min_child_pos
            self.bubble_down(key, position)

    def swap(self, position_1: int, position_2: int) -> None:
        i, j = (position_1 - 1, position_2 - 1)
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp

    def parent_position(self, position: int) -> int:
        return position // 2

    def min_child_position(self, position: int) -> Optional[int]:
        (pos_1, pos_2) = (2 * position, 2 * position + 1)
        try:
            child_1 = self.heap[pos_1 - 1]
        except IndexError:
            return None
        try:
            child_2 = self.heap[pos_2 - 1]
        except IndexError:
            return pos_1
        min_child_pos = pos_1 if child_1 < child_2 else pos_2
        return min_child_pos
