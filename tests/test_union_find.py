import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '../..'))
import unittest
from union_find import UnionFind, Node

class TestUnionFind(unittest.TestCase):
    def test_find(self):
        """
        model a graph with two partitions:
        a <- b <- c

        d <- e
        """
        test_union_find = UnionFind()
        # override internal data structure to test find
        test_union_find.union_find = {
            'c': Node('c', parent_label='b', rank=0),
            'b': Node('b', parent_label='a', rank=1),
            'a': Node('a', parent_label='a', rank=2),
            'e': Node('e', parent_label='d', rank=0),
            'd': Node('d', parent_label='d', rank=1),
        }
        expected_leaders = [
            ('c', 'a'),
            ('b', 'a'),
            ('a', 'a'),
            ('e', 'd'),
            ('d', 'd'),
        ]
        for child, expected_leader in expected_leaders:
            self.assertEqual(test_union_find.find(child), expected_leader)
