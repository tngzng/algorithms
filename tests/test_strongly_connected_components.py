import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '../..'))
import unittest
import strongly_connected_components as scc

class TestStronglyConnectedComponents(unittest.TestCase):
    def test_reverse_graph(self):
        # input graph:
        # 1-->2-->3
        # ^   |
        # |   v
        # 5<--6
        graph = {
            1: [2],
            2: [3, 6],
            6: [5],
            5: [1],
            3: [],
        }
        reversed_graph = scc.reverse_graph(graph)
        # expected output graph:
        # 1<--2<--3
        # |   ^
        # v   |
        # 5-->6
        expected_graph = {
            1: [5],
            2: [1],
            6: [2],
            5: [6],
            3: [2],
        }
        for node in reversed_graph:
            self.assertListEqual(reversed_graph[node], expected_graph[node])

    def test_strongly_connected_components(self):
        # input graph:
        # 1-->2-->3<--4
        # ^   |   |   ^
        # |   v   v   |
        # 5<--6   7-->8

        g = {
            1: [2],
            2: [3, 6],
            6: [5],
            5: [1],
            3: [7],
            4: [3],
            8: [4],
            7: [8],
        }

        res = scc.strongly_connected_components(g)
        for component in res:
            component.sort()
        assert [1, 2, 5, 6] in res
        assert [3, 4, 7, 8] in res

if __name__ == '__main__':
    unittest.main()