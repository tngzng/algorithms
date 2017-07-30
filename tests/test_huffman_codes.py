import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '../..'))
import unittest
from huffman_codes import huffman_codes, Node, Queue, _compare_and_pop_smallest, \
                          _traverse_children_and_assign_codes


class TestHuffmanCodes(unittest.TestCase):
    def test_compare_and_pop_smallest__first_q_smaller(self):
        q_1 = Queue()
        q_1.enqueue((None, 1))
        q_2 = Queue()
        q_2.enqueue((None, 2))
        output = _compare_and_pop_smallest(q_1, q_2)
        self.assertEqual(output[1], 1)

    def test_compare_and_pop_smallest__second_q_smaller(self):
        q_1 = Queue()
        q_1.enqueue((None, 1))
        q_2 = Queue()
        q_2.enqueue((None, 2))
        output = _compare_and_pop_smallest(q_2, q_1)
        self.assertEqual(output[1], 1)

    def test_compare_and_pop_smallest__first_q_empty(self):
        q_1 = Queue()
        q_2 = Queue()
        q_2.enqueue((None, 2))
        output = _compare_and_pop_smallest(q_2, q_1)
        self.assertEqual(output[1], 2)

    def test_compare_and_pop_smallest__second_q_empty(self):
        q_1 = Queue()
        q_1.enqueue((None, 1))
        q_2 = Queue()
        output = _compare_and_pop_smallest(q_2, q_1)
        self.assertEqual(output[1], 1)

    def test_traverse_children_and_assign_codes(self):
        pass

    def test_huffman_codes(self):
        pass
