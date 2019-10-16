import unittest

from algorithms.connected_components import get_connected_components


class TestConnectedComponents(unittest.TestCase):
    def test_get_connected_components(self):
        # input graph:
        # 1---2   3---4   9
        # | X |   | X |
        # 5---6   7---8

        g = {
            1: [2,5,6],
            2: [1,5,6],
            6: [5,1,2],
            5: [1,2,6],
            3: [7,8,4],
            4: [3,7,8],
            8: [7,3,4],
            7: [3,4,8],
            9: []
        }

        res = get_connected_components(g)
        for component in res:
            component.sort()
        assert [1, 2, 5, 6] in res
        assert [3, 4, 7, 8] in res
        assert [9] in res
