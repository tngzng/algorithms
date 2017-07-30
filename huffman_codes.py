def huffman_codes(char_frequencies):
    parent_q = Queue()
    node_q = Queue()
    for char, frequency in sorted(char_frequencies, key=lambda x: x[1]):
        node_q.enqueue((Node(label=char), frequency))

    while True:
        parent_node = Node()

        node_frequency_a = _compare_and_pop_smallest(parent_q, node_q)
        node_a = node_frequency_a[0]
        parent_node.update_left_child(node_a)
        frequency_a = node_frequency_a[1]
        combined_frequency = frequency_a
        parent_label = node_a.label

        node_frequency_b = _compare_and_pop_smallest(parent_q, node_q)
        if node_frequency_b:
            node_b = node_frequency_b[0]
            parent_node.update_right_child(node_b)
            frequency_b = node_frequency_b[1]
            combined_frequency = combined_frequency + frequency_b
            parent_label = '{}{}'.format(parent_label, node_b.label)

        parent_node.update_label(parent_label)
        if not len(parent_q) and not len(node_q):
            break

        parent_q.enqueue((parent_node, combined_frequency))

    code_dict = {}
    _traverse_children_and_assign_codes(parent_node, code_dict)
    return code_dict


def _traverse_children_and_assign_codes(parent, code_dict):
    # when we hit a leaf, add it's binary code to our final output dict
    if not parent.left_child and not parent.right_child:
        code_dict[parent.label] = parent.binary_code

    # TODO: update to return codes as a bitarray for memory savings
    if parent.left_child:
        left_code = '{parent_code}0'.format(parent_code=parent.binary_code)
        parent.left_child.update_code(left_code)
        _traverse_children_and_assign_codes(parent.left_child, code_dict)

    if parent.right_child:
        right_code = '{parent_code}1'.format(parent_code=parent.binary_code)
        parent.right_child.update_code(right_code)
        _traverse_children_and_assign_codes(parent.right_child, code_dict)


def _compare_and_pop_smallest(node_q_1, node_q_2):
    if not len(node_q_1) and not len(node_q_2):
        return None

    if not len(node_q_1):
        return node_q_2.dequeue()

    if not len(node_q_2):
        return node_q_1.dequeue()

    if node_q_1.peak()[1] < node_q_2.peak()[1]:
        return node_q_1.dequeue()
    else:
        return node_q_2.dequeue()


class Node:
    def __init__(self, label='', parent_node=None, left_child=None, right_child=None, binary_code=''):
        self.label = label
        self.parent_node = parent_node
        self.left_child = left_child
        self.right_child = right_child
        self.binary_code = binary_code

    def update_parent(self, parent_node):
        self.parent_node = parent_node

    def update_left_child(self, left_child):
        self.left_child = left_child

    def update_right_child(self, right_child):
        self.right_child = right_child

    def update_code(self, binary_code):
        self.binary_code = binary_code

    def update_label(self, label):
        self.label = label


class Queue:
    def __init__(self):
        self._queue = []

    def peak(self):
        return self._queue[-1]

    def enqueue(self, el):
        self._queue.insert(0, el)

    def dequeue(self):
        return self._queue.pop()

    def __len__(self):
        return len(self._queue)

    def __str__(self):
        return self._queue.__str__()

    def __repr__(self):
        return self._queue.__repr__()