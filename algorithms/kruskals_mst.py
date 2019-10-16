from typing import List, Tuple

from algorithms.union_find import UnionFind


def kruskals_mst(edge_list: List[Tuple[str, str, int]]):
    r"""
    for a given edge_list representing an undirected graph,
    return an edge_list representing the minimum spanning tree (mst) for the input graph.

    the input edge_list should consist of tuples as follows: (node_a, node_b, edge_weight).
    for example, the graph below:
              a
          5  / \ 1
            /   \
           b --- c
             2

    should be represented by the edge_list:
    [('a', 'b', 5), ('a', 'c', 1), ('b', 'c', 2)]

    where the node order doesn't matter, since this is an undirected graph.

    an mst is the tree with the lowest summed edge weights that connects all a graph's nodes.
    for example, we would expect this mst to be returned for the input graph above:
    [('a', 'c', 1), ('b', 'c', 2)]
    """
    mst = []
    node_tuples = [(tup[0], tup[1]) for tup in edge_list]
    unique_nodes = {tup_el for tup in node_tuples for tup_el in tup}
    _union_find = UnionFind(unique_nodes)
    sorted_edges = sorted(edge_list, key=lambda x: x[2])

    for edge in sorted_edges:
        leader_a = _union_find.find(edge[0])
        leader_b = _union_find.find(edge[1])
        # if the leaders are the same, the nodes are in the same partition of the union find.
        # that means adding the current edge to the mst would create a cycle, so we reject it.
        if leader_a == leader_b:
            continue

        _union_find.union(leader_a, leader_b)
        mst.append(edge)

    return mst
