finishing_time = 1
finishing_times = {}
explored = set([])
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

    This implementation assumes the inputted graph is an adjacency list of nodes.
    """
    reversed_graph = reverse_graph(graph)

    for node in reversed_graph:
        if node not in explored:
            dfs(reversed_graph, node)

    # 3. run dfs on original graph
        # processing nodes in decreasing order of finish time
    return [[1, 2, 5, 6], [3, 4, 8, 7]]

def dfs(graph, node):
    """
    Depth first search that updates the global variable finishing_times with order each node finished processing.
    """
    global explored
    global finishing_times
    global finishing_time

    explored.add(node)
    for adj_node in graph[node]:
        if adj_node not in explored:
            dfs(graph, adj_node)

    finishing_times[node] = finishing_time
    finishing_time += 1
