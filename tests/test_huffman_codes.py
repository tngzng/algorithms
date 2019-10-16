import unittest

from algorithms.huffman_codes import (
    huffman_codes,
    HuffmanNode,
    Queue,
    _compare_and_pop_smallest,
    _traverse_children_and_assign_codes
)


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
        q_1.enqueue((None, 2))
        q_2 = Queue()
        q_2.enqueue((None, 1))
        output = _compare_and_pop_smallest(q_1, q_2)
        self.assertEqual(output[1], 1)

    def test_compare_and_pop_smallest__first_q_empty(self):
        q_1 = Queue()
        q_2 = Queue()
        q_2.enqueue((None, 2))
        output = _compare_and_pop_smallest(q_1, q_2)
        self.assertEqual(output[1], 2)

    def test_compare_and_pop_smallest__second_q_empty(self):
        q_1 = Queue()
        q_1.enqueue((None, 1))
        q_2 = Queue()
        output = _compare_and_pop_smallest(q_1, q_2)
        self.assertEqual(output[1], 1)

    def test_traverse_children_and_assign_codes(self):
        """
        test the following binary tree
              a
             / \
            /   \
           b     c
          / \
         d   e
        """
        expected_code_dict = {
            'd': '00',
            'e': '01',
            'c': '1',
        }

        c = HuffmanNode(label='c')
        d = HuffmanNode(label='d')
        e = HuffmanNode(label='e')
        b = HuffmanNode(label='b', left_child=d, right_child=e)
        a = HuffmanNode(label='a', left_child=b, right_child=c)

        code_dict = {}
        _traverse_children_and_assign_codes(a, code_dict)
        self.assertDictEqual(code_dict, expected_code_dict)

    def test_huffman_codes(self):
        char_frequencies = [
            ('a', 3),
            ('b', 2),
            ('c', 6),
            ('d', 8),
            ('e', 2),
            ('f', 6),
        ]

        expected_code_lens = {
            'a': 3,
            'b': 4,
            'c': 2,
            'd': 2,
            'e': 4,
            'f': 2,
        }

        code_dict = huffman_codes(char_frequencies)
        for char, code in code_dict.items():
            self.assertEqual(len(code), expected_code_lens[char])
