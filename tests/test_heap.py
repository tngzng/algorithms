import unittest

from algorithms.heap import Heap


class TestHeap(unittest.TestCase):
    def test_insert(self):
        heap = Heap()
        heap.insert(4)
        self.assertEqual(heap.heap, [4])
        heap.insert(3)
        self.assertEqual(heap.heap, [3, 4])
        heap.insert(2)
        self.assertFalse(self.heap_violation(heap.heap))
        heap.insert(1)
        self.assertFalse(self.heap_violation(heap.heap))

    def test_extract_min(self):
        heap = Heap()
        heap.insert(4)
        heap.insert(3)
        heap.insert(2)
        heap.insert(1)
        min = heap.extract_min()
        self.assertEqual(min, 1)
        self.assertFalse(self.heap_violation(heap.heap))
        min = heap.extract_min()
        self.assertEqual(min, 2)
        self.assertFalse(self.heap_violation(heap.heap))

    def heap_violation(self, heap):
        for i in range(len(heap)):
            position = i + 1
            key = heap[position - 1]
            parent_position = self.parent_position(position)
            if not parent_position:
                continue
            parent = heap[parent_position - 1]
            if parent > key:
                return True
        return False

    def parent_position(self, position):
        return position // 2
