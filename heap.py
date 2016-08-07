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

    def swap(self, position_1, position_2):
        i, j = (position_1 - 1, position_2 - 1)
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp

    def parent_position(self, position):
        return position / 2
