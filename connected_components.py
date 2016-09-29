from collections import deque

def get_connected_components(g):
    """
    Return an array of arrays, each representing a connected component.

    :param dict g: graph represented as an adjacency list where all nodes are labeled 1 to n.
    :returns: array of arrays, each representing a connected component.
    """
    connected_components = []
    explored = set([])
    node_count = len(g)
    for i in xrange(1, node_count + 1):
        if i not in explored:
            connected_component = find_connected_component(g, i, explored)
            connected_components.append(connected_component)
    return connected_components

def find_connected_component(g, node, explored):
    """
    Breadth first search implementation that returns a connected component for a given starting node.

    :param dict g: graph represented as an adjacency list.
    :param int node: a node label representing the starting node, can also be a string or another hashable type.
    :param set explored: the nodes that have already been searched.
    :returns: an array, representing the connected component for the given starting node.
    """
    q = deque([node])
    connected_component = [node]
    explored.add(node)
    while q:
        node = q.popleft()
        for adj_node in g[node]:
            if adj_node not in explored:
                explored.add(adj_node)
                connected_component.append(adj_node)
                q.append(adj_node)
    return connected_component
