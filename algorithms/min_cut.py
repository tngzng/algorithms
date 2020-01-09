import math
import random
import sys
from typing import Dict, List, Set, Tuple


def min_cut(g: Dict[str, List[str]]) -> int:
    """
    Return a min cut with probability of failure 1/n.

    :param dict g: graph represented as an adjacency list.
    :returns: int representing min cut.
    """
    n = len(g)
    # repeat n choose 2 * ln n times
    runs = int((n * (n - 1) / 2) * math.log(n))
    minimum = sys.maxsize
    for i in range(0, runs):
        temp_g = g
        res = random_contraction(temp_g)
        if res < minimum:
            minimum = res

    return minimum


def random_contraction(g: Dict[str, List[str]]) -> int:
    """
    Return a potential minimum cut from a graph.

    :param dict g: graph we are contracting represented as an adjacency list.
    :returns: int representing a potential min cut.
    """
    edges = list(get_edgelist(g))

    while len(g) > 2:
        rand = random.randrange(0, len(edges))
        (u, v) = edges.pop(rand)
        g[u] = g[u] + g[v]  # contract u and v
        g[u] = [adj for adj in g[u] if adj not in [u, v]]  # remove self loops from nodes
        del g[v]

        # update occurrences of v to u
        for i, edge in enumerate(edges):
            if v in edge:
                edge = tuple([node if node != v else u for node in edge])
                edges[i] = edge

        # remove self loops from edges
        edges = [(x, y) for (x, y) in edges if x != y]

    return len(edges)


def get_edgelist(g: Dict[str, List[str]]) -> Set[Tuple[str, ...]]:
    """
    Return a list of edges from a graph represented as an adjacency list.

    :param dict g: graph represented as an adjacency list.
    :returns: list of tuples.
    """
    edges = set([])
    for node in g:
        for adj in g[node]:
            # sort to deduplicate
            sorted_tuple = tuple(sorted((node, adj)))
            edges.add(sorted_tuple)

    return edges


# TODO: since min_cut does not succeed all the time, determine how to write unit test

# model this graph:
# 'a'---'b'---'c'---'d'
# |   X  |     |  X  |
# 'e'---'f'---'g'---'h'

g = {
    'a': ['b', 'e', 'f'],
    'b': ['a', 'e', 'f', 'c'],
    'c': ['b', 'g', 'h', 'd'],
    'd': ['c', 'g', 'h'],
    'h': ['g', 'c', 'd'],
    'g': ['f', 'c', 'd', 'h'],
    'f': ['e', 'a', 'b', 'g'],
    'e': ['a', 'b', 'f']
}

print(min_cut(g))
