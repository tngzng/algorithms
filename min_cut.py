import random

def random_contraction(g):
    """
    Return a potential minimum cut from a graph.

    :param dict g: graph we are contracting represented as an edgelist.
    :returns: int representing a potential min cut.
    """
    edges = get_edgelist(g)

    while len(g) > 2:
        rand = random.randrange(0, len(edges))
        (u,v) = edges.pop(rand)
        g[u] = g[u] + g[v] # contract u and v
        g[u] = [adj for adj in g[u] if adj not in [u, v]] # remove self loops
        del g[v]

        # update occurrences of v to u
        for i, edge in enumerate(edges):
            if v in edge:
                edge = tuple([node if node != v else u for node in edge])
                edges[i] = edge

    return len(edges)

def get_edgelist(g):
    edges = set([])
    for node in g:
        for adj in g[node]:
            # sort to deduplicated
            sorted_tuple = tuple(sorted((node, adj)))
            edges.add(sorted_tuple)

    return list(edges)


# model this graph:
# 'a'---'b'---'c'---'d'
# |   X  |     |  X  |
# 'e'---'f'---'g'---'h'
g = {
    'a': ['b','e','f'],
    'b': ['a','e','f','c'],
    'c': ['b','g','h','d'],
    'd': ['c','g','h'],
    'h': ['g','c','d'],
    'g': ['f','c','d','h'],
    'f': ['e','a','b','g'],
    'e': ['a','b','f']
}

# model this graph:
# 'a'---'b'
# |   /  |
# 'e'---'f'
# g = {
#     'a': ['e','b'],
#     'b': ['a','e','f'],
#     'f': ['b','e'],
#     'e': ['a','b','f']
# }

for i in range(0,1000):
    print random_contraction(g)