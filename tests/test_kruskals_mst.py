import unittest

from algorithms.kruskals_mst import kruskals_mst


class TestKruskalsMST(unittest.TestCase):
    def test_kruskals_mst(self):
        r"""
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
