import unittest

from algorithms.strongly_connected_components import StronglyConnectedComponents


class TestStronglyConnectedComponents(unittest.TestCase):
    def setUp(self):
        self.scc = StronglyConnectedComponents()

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
        reversed_graph = self.scc.reverse_graph(graph)
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
            self.assertEqual(sorted(reversed_graph[node]), sorted(expected_graph[node]))

    def test_dfs_updates_finishing_times(self):
        # input graph:
        # 1-->2-->3-->4
        graph = {
            1: [2],
            2: [3],
            3: [4],
            4: [],
        }
        self.scc.dfs(graph, 1)
        expected_order = [4, 3, 2, 1]
        self.assertEqual(self.scc.finishing_order, expected_order)

    def test_dfs_updates_components(self):
        # input graph:
        # 1-->2   3<--4
        # ^   |   |   ^
        # |   v   v   |
        # 5<--6   7-->8
        graph = {
            1: [2],
            2: [6],
            6: [5],
            5: [1],
            3: [7],
            4: [3],
            8: [4],
            7: [8],
        }
        self.scc.source_node = 3
        self.scc.dfs(graph, 3)
        self.scc.source_node = 1
        self.scc.dfs(graph, 1)
        expected_components = {
            3: [3, 4, 7, 8],
            1: [1, 2, 5, 6],
        }
        for source_node in self.scc.components:
            self.assertEqual(sorted(self.scc.components[source_node]),
                             sorted(expected_components[source_node]))

    def test_strongly_connected_components(self):
        # input graph:
        # 1-->2-->3<--4
        # ^   |   |   ^
        # |   v   v   |
        # 5<--6   7-->8

        graph = {
            1: [2],
            2: [3, 6],
            6: [5],
            5: [1],
            3: [7],
            4: [3],
            8: [4],
            7: [8],
        }

        res = self.scc.strongly_connected_components(graph)
        for component in res:
            component.sort()
        assert [1, 2, 5, 6] in res
        assert [3, 4, 7, 8] in res
