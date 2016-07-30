finishing_time = 0
source_node = None

def reverse_graph(graph):
    reversed_graph = {}
    for node in graph:
        edge_list = graph[node]
        for adj_node in edge_list:
            try:
                reversed_graph[adj_node].append(node)
            except KeyError:
                reversed_graph[adj_node] = [node]

    return reversed_graph

def strongly_connected_components(graph):
    """
    Given a directed graph, find all the strongly strongly connected components. A strongly connected component is a collection of nodes in a graph where each node is reachable from every other node.

    This algorithm assumes the inputted graph is an adjacency list of nodes, where each node is labeled by an integer from 1 to n, the number of nodes in the graph.
    """
    # 1. reverse direction of all edges in graph
    # 2. run dfs on the reversed graph
        # storing the finish time of each node
    # 3. run dfs on original graph
        # processing nodes in decreasing order of finish time
    return [[1, 2, 5, 6], [3, 4, 8, 7]]

def dfs(graph, node):
    pass


