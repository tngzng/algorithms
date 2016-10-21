from heapq import heappush, heappop

def dijkstra(g, start):
    """
    return cost of the shortest path from the start node to all other nodes in g
    """
    discovered = set([start])
    processed = set([])
    res = {}
    h = [(0, start)] # heap h stores (cost, node) from the start node
    heap_entries = {start: (0, start)}

    while h:
        (cost, node) = heappop(h)
        processed.add(node)
        res[node] = cost

        for adj_node, edge_weight in g[node]:
            if adj_node not in discovered:
                discovered.add(adj_node)
                heappush(h, (cost + edge_weight, adj_node))
                heap_entries[adj_node] = (cost + edge_weight, adj_node)
            elif adj_node not in processed:
                # TODO: remove takes O(N) time -- find faster way to delete from heap
                prev_weight, _ = heap_entries[adj_node]
                h.remove((prev_weight, _))
                min_weight = min(prev_weight, cost + edge_weight)
                heappush(h, (min_weight, adj_node))
                heap_entries[adj_node] = (min_weight, adj_node)

    return res

# TODO: move driver tests to unit tests

#        a
#    5  / \  1
#      /   \
#     b --- c
#  3 /   2
#   d

g = {
    'a': [('b', 5), ('c', 1)],
    'b': [('a', 5), ('c', 2), ('d', 3)],
    'c': [('a', 1), ('b', 2)],
    'd': [('b', 3)],
}

res = dijkstra(g, 'a')
print res
expected_res = {
    'a': 0,
    'b': 3,
    'c': 1,
    'd': 6,
}

for k in expected_res.iterkeys():
    assert expected_res[k] == res[k]

print 'End of driver test!'