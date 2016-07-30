finishing_time = 1
finishing_order = []
explored = set([])
source_node = None
components = {}

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
    Given a directed graph, return an array of its strongly connected components. A strongly connected component is a collection of nodes where each node is reachable from every other node.

    This implementation assumes the inputted graph is an adjacency list of nodes.
    """
    global explored
    global source_node

    reversed_graph = reverse_graph(graph)
    for node in reversed_graph:
        if node not in explored:
            dfs(reversed_graph, node)

    explored = set([])
    for node in reversed(finishing_order):
        if node not in explored:
            source_node = node
            dfs(graph, node)

    res = []
    for source_node in components:
        res.append(components[source_node])
    return res

def dfs(graph, node):
    """
    Depth first search that:
    1. Updates the global variable finishing_order with order each node finished processing.
    2. Updates the global variable components, associating each node with the source node it was originally called from.
    """
    global explored
    global finishing_order
    global finishing_time
    global components

    explored.add(node)
    try:
        components[source_node].append(node)
    except KeyError:
        components[source_node] = [node]
    for adj_node in graph[node]:
        if adj_node not in explored:
            dfs(graph, adj_node)

    finishing_order.append(node)
    finishing_time += 1
