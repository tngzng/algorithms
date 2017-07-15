class UnionFind:
    def __init__(self, node_labels=[]):
        self._union_find = {}
        for node_label in node_labels:
            self._union_find[node_label] = Node(node_label, parent_label=node_label)

    def find(self, node_label):
        # TODO add lazy path compression
        node = self._union_find[node_label]
        parent = self._union_find[node.parent_label]
        while True:
            if parent.label == node.label:
                # the partition leader's parent is itself
                return parent.label
            else:
                node = parent
                parent = self._union_find[parent.parent_label]

    def union(self, node_label_a, node_label_b):
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
    def __init__(self, label, parent_label=None, rank=0):
        self._label = label
        self._parent_label = parent_label
        self._rank = rank

    @property
    def parent_label(self):
        return self._parent_label

    @property
    def label(self):
        return self._label

    @property
    def rank(self):
        return self._rank

    def set_parent_label(self, parent_label):
        self._parent_label = parent_label

    def set_rank(self, rank):
        self._rank = rank
