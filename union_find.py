class UnionFind:
    def __init__(self, node_labels=[]):
        self.union_find = {}
        for node_label in node_labels:
            self.union_find[node_label] = Node(node_label, parent_label=node_label)

    def find(self, node_label):
        node = self.union_find[node_label]
        parent = self.union_find[node.parent_label]
        while True:
            if parent.label == node.label:
                # the partition leader's parent is itself
                return parent.label
            else:
                node = parent
                parent = self.union_find[parent.parent_label]

    def union(self, node_a, node_b):
        pass


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