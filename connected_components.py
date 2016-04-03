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
            connected_component = bfs(g, i, explored)
            connected_components.append(connected_component)
    return connected_components

def bfs(g, node, explored):
    pass

# model this graph:
# 1---2   3---4
# | X |   | X |
# 5---6   7---8

g = {
    1: [2,5,6],
    2: [1,5,6],
    3: [7,8,4],
    4: [3,7,8],
    8: [7,3,4],
    7: [3,4,8],
    6: [5,1,2],
    5: [1,2,6]
}

print get_connected_components(g)