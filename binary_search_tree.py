class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def min(self, start_node=None):
        if not start_node:
            start_node = self.root
        if not start_node:
            return None # empty tree

        last_taversed_node = start_node
        while last_taversed_node.left_child:
            last_taversed_node = last_taversed_node.left_child

        return last_taversed_node

    def max(self, start_node=None):
        if not start_node:
            start_node = self.root
        if not start_node:
            return None # empty tree

        last_taversed_node = start_node
        while last_taversed_node.right_child:
            last_taversed_node = last_taversed_node.right_child

        return last_taversed_node

    def prev(self, node):
        # if node has left subtree, return max from that subtree
        if node.left_child:
            return self.max(start_node=node.left_child)

        # traverse parents until a parent with a lower value is reached
        next_node = node
        while next_node:
            if next_node.label < node.label:
                return next_node
            next_node = next_node.parent

        return None # input node is the min

    def next(self, node):
        # if node has right subtree, return min from that subtree
        if node.right_child:
            return self.min(start_node=node.right_child)

        # traverse parents until a parent with a higher value is reached
        next_node = node
        while next_node:
            if next_node.label > node.label:
                return next_node
            next_node = next_node.parent

        return None # input node is the max

    def traverse_in_order(self):
        min_node = self.min()
        if min_node:
            next_node = min_node
            while next_node:
                yield next_node
                next_node = self.next(next_node)

    def search(self, start_node, target_key):
        """
        returns a tuple representing (was_found, last_traversed_node)
        """
        start_key = start_node.label
        if start_key < target_key:
            child_node = start_node.right_child
        else:
            child_node = start_node.left_child

        if child_node == None:
            return (False, start_node)

        child_key = child_node.label
        if child_key == target_key:
            return (True, start_node)

        return self.search(child_node, target_key)

    def insert(self, key):
        if not self.root:
            self.root = BinarySearchNode(key, parent=None)
            return self.root

        res = self.search(self.root, key)
        found, last_traversed_node = res

        if found:
            return None # duplicate keys not supported

        return BinarySearchNode(key, parent=last_traversed_node)


class BinarySearchNode(object):
    def __init__(self, label, parent=None, left_child=None, right_child=None):
        self.label = label
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child
        self.update_parent()

    def __str__(self):
        return '{} {}'.format(self.__class__.__name__, self.label)

    def update_parent(self):
        if not self.parent:
            return # root node
        parent_label = self.parent.label
        if parent_label < self.label:
            self.parent.right_child = self
        else:
            self.parent.left_child = self
