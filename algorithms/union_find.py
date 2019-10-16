from typing import List, Optional


class UnionFind:
    """
    The union find data structure maintains partitions in a graph

    For ex, the graph below has two partitions. One with nodes 'a', 'b', and 'c'.
    The other with nodes 'e' and 'd'

    a <- b <- c

    d <- e
    """

    def __init__(self, node_labels: List[str] = []) -> object:
        self._union_find = {}
        for node_label in node_labels:
            self._union_find[node_label] = Node(node_label, parent_label=node_label)

    def _update_leaders(self, node_labels: List[str], leader: str) -> None:
        for node_label in node_labels:
            self._union_find[node_label].set_parent_label(leader)

    def find(self, node_label: str) -> str:
        """
        Given a node label, return the label associated with the leader node for its partition

        For ex, the leader node of 'c' in the partition below is 'a'

        a <- b <- c
        """
        node = self._union_find[node_label]
        parent = self._union_find[node.parent_label]
        path_to_leader = []
        while True:
            path_to_leader.append(node.label)
            if parent.label == node.label:
                # the partition leader's parent is itself
                leader = parent.label
                self._update_leaders(path_to_leader, leader)
                return leader
            else:
                node = parent
                parent = self._union_find[parent.parent_label]

    def union(self, node_label_a: str, node_label_b: str) -> None:
        """
        Given two node labels, fuse the partitions associated with each node together

        For example, the partitions
        a <- b <- c

        d <- e

        Would become
        a <- b <- c
        ^
        |
        d <- e

        With the union of nodes 'c' and 'e'
        """
        leader_label_a = self.find(node_label_a)
        leader_label_b = self.find(node_label_b)
        leader_a = self._union_find[leader_label_a]
        leader_b = self._union_find[leader_label_b]
        if leader_a.rank > leader_b.rank:
            leader_b.set_parent_label(leader_label_a)
        elif leader_a.rank == leader_b.rank:
            leader_a.set_parent_label(leader_label_b)
            # increment the leader's rank if it's merged with a subgraph of the same depth
            leader_b.set_rank(leader_b.rank + 1)
        else:
            leader_a.set_parent_label(leader_label_b)


class Node:
    def __init__(self, label: str, parent_label: Optional[str] = None, rank: int = 0) -> None:
        self._label = label
        self._parent_label = parent_label
        self._rank = rank

    @property
    def parent_label(self) -> str:
        return self._parent_label

    @property
    def label(self) -> str:
        return self._label

    @property
    def rank(self) -> int:
        return self._rank

    def set_parent_label(self, parent_label: str) -> None:
        self._parent_label = parent_label

    def set_rank(self, rank: int) -> None:
        self._rank = rank
