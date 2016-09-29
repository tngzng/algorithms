import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '../..'))
import unittest
from topological_sort import topological_sort


class TestTopologicalSort(unittest.TestCase):
    def test_topological_sort(self):
        # input graph:
        # a -> b -> c
        g = {
            'a': ['b'],
            'b': ['c'],
            'c': [],
        }

        topological_ordering = topological_sort(g)
        assert topological_ordering['a'] < topological_ordering['b']
        assert topological_ordering['b'] < topological_ordering['c']

        # input graph:
        # c -------> d
        # ^          ^
        # |          |
        # a -------> b
        g = {
            'a': ['b', 'c'],
            'b': ['d'],
            'c': ['d'] ,
            'd': [],
        }

        topological_ordering = topological_sort(g)
        assert topological_ordering['a'] < topological_ordering['b']
        assert topological_ordering['a'] < topological_ordering['c']
        assert topological_ordering['c'] < topological_ordering['d']
        assert topological_ordering['b'] < topological_ordering['d']
