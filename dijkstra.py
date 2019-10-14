from typing import Mapping, List
from heapq import heappush, heappop


def dijkstra(g: Mapping[int, List[int]], start: str) -> Mapping[str, int]:
    """
    return cost of the shortest path from the start node to all other nodes in g
    """
    discovered = set([start])
    res = {}
    h = [(0, start)] # heap h stores (cost, node) from the start node
    heap_entries = {start: (0, start)}

    while h:
        (cost, node) = heappop(h)
        res[node] = cost

        for adj_node, edge_weight in g[node]:
            if adj_node not in discovered:
                discovered.add(adj_node)
                heappush(h, (cost + edge_weight, adj_node))
                heap_entries[adj_node] = (cost + edge_weight, adj_node)
            elif adj_node not in res:
                # TODO: remove takes O(N) time -- find faster way to delete from heap
                prev_weight, _ = heap_entries[adj_node]
                h.remove((prev_weight, _))
                min_weight = min(prev_weight, cost + edge_weight)
                heappush(h, (min_weight, adj_node))
                heap_entries[adj_node] = (min_weight, adj_node)

    return res
