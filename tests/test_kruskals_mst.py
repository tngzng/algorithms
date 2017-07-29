import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '../..'))
import unittest
from kruskals_mst import kruskals_mst

class TestKruskalsMST(unittest.TestCase):
    def test_kruskals_mst(self):
        """
        model the graph:
              a
          5  / \  1
            /   \
           b --- c
             2
        """
        input_graph = [('a', 'b', 5), ('a', 'c', 1), ('b', 'c', 2)]
        output = kruskals_mst(input_graph)
        expected = [('a', 'c', 1), ('b', 'c', 2)]
        self.assertEqual(output, expected)
