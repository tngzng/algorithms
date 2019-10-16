from typing import Mapping, List


class StronglyConnectedComponents:
    def __init__(self) -> None:
        self.reset_dfs_vars()

    def reset_dfs_vars(self) -> None:
        self.finishing_time = 1
        self.finishing_order = []
        self.explored = set([])
        self.source_node = None
        self.components = {}

    def reverse_graph(self, graph: Mapping[int, List[int]]) -> Mapping[int, List[int]]:
        reversed_graph = {}
        for node in graph:
            edge_list = graph[node]
            for adj_node in edge_list:
                try:
                    reversed_graph[adj_node].append(node)
                except KeyError:
                    reversed_graph[adj_node] = [node]

        return reversed_graph

    def strongly_connected_components(self, graph: Mapping[int, List[int]]) -> List[int]:
        """
        Given a directed graph, return an array of its strongly connected components.
        A strongly connected component is a collection of nodes where each node is reachable from every other node.

        This implementation assumes the inputted graph is an adjacency list of nodes.
        """
        reversed_graph = self.reverse_graph(graph)
        for node in reversed_graph:
            if node not in self.explored:
                self.dfs(reversed_graph, node)
        reversed_order = reversed(self.finishing_order)
        self.reset_dfs_vars()

        for node in reversed_order:
            if node not in self.explored:
                self.source_node = node
                self.dfs(graph, node)

        res = self.components.values()
        self.reset_dfs_vars()
        return res

    def dfs(self, graph: Mapping[int, List[int]], node: int) -> None:
        """
        Depth first search that:
        1. Updates the global variable finishing_order with order each node finished processing.
        2. Updates the global variable components, associating each node with its source node.
        """
        self.explored.add(node)
        try:
            self.components[self.source_node].append(node)
        except KeyError:
            self.components[self.source_node] = [node]
        for adj_node in graph[node]:
            if adj_node not in self.explored:
                self.dfs(graph, adj_node)

        self.finishing_order.append(node)
        self.finishing_time += 1
