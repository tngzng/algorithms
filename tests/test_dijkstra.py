import unittest

from algorithms.dijkstra import dijkstra


class TestDijkstra(unittest.TestCase):
    def test_insert(self):
        r"""
        test the following graph

              a
          5  / \  1
            /   \
           b --- c
        3 /   2
         d
        """
        g = {
            'a': [('b', 5), ('c', 1)],
            'b': [('a', 5), ('c', 2), ('d', 3)],
            'c': [('a', 1), ('b', 2)],
            'd': [('b', 3)],
        }

        res = dijkstra(g, 'a')
        expected_res = {
            'a': 0,
            'b': 3,
            'c': 1,
            'd': 6,
        }

        self.assertEqual(res, expected_res)
