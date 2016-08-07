class Heap(object):
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        position = len(self.heap)
        self.bubble_up(key, position)

    def bubble_up(self, key, position):
        parent_position = self.parent_position(position)
        if not parent_position:
            return
        parent = self.heap[parent_position - 1]
        if parent and parent > key:
            self.swap(position, parent_position)
            position = parent_position
            self.bubble_up(key, position)

    def extract_min(self):
        res = self.heap[0]
        self.heap[0] = self.heap.pop()
        position = 1
        key = self.heap[position - 1]
        self.bubble_down(key, position)
        return res

    def bubble_down(self, key, position):
        min_child_pos = self.min_child_position(position)
        if not min_child_pos:
            return
        min_child = self.heap[min_child_pos - 1]
        if key > min_child:
            self.swap(position, min_child_pos)
            position = min_child_pos
            self.bubble_down(key, position)

    def swap(self, position_1, position_2):
        i, j = (position_1 - 1, position_2 - 1)
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp

    def parent_position(self, position):
        return position / 2

    def min_child_position(self, position):
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
