def huffman_codes(char_frequencies):
    """
    given an alphabet where each character has a different frequency of occurring,
    produce a representation in binary for each character that minimizes the memory
    needed to encode something in the alphabet

    :param (list) char_frequencies: a list of tuples representing chars and their frequencies
    :returns (dict): a dict representing chars and their binary encodings
    """
    # construct a queue of nodes, with highest priority given to the lowest frequency chars
    node_q = Queue()
    for char, frequency in sorted(char_frequencies, key=lambda x: x[1]):
        node_q.enqueue((HuffmanNode(label=char), frequency))

    # build a binary tree, successively merging nodes into larger subtrees
    subtree_q = Queue()
    while True:
        parent_node = HuffmanNode()

        # at each step choose the two lowest frequency nodes and merge them
        # into a subtree under a new parent_node
        left_node_frequency = _compare_and_pop_smallest(subtree_q, node_q)
        right_node_frequency = _compare_and_pop_smallest(subtree_q, node_q)

        left_node = left_node_frequency[0]
        parent_node.update_left_child(left_node)
        left_frequency = left_node_frequency[1]
        combined_frequency = left_frequency
        parent_label = left_node.label

        if right_node_frequency:
            right_node = right_node_frequency[0]
            parent_node.update_right_child(right_node)
            right_frequency = right_node_frequency[1]
            combined_frequency = combined_frequency + right_frequency
            parent_label = '{}{}'.format(parent_label, right_node.label)

        parent_node.update_label(parent_label)

        # break when the binary tree has been fully constructed
        if not len(subtree_q) and not len(node_q):
            break

        subtree_q.enqueue((parent_node, combined_frequency))

    code_dict = {}
    _traverse_children_and_assign_codes(parent_node, code_dict)
    return code_dict


def _traverse_children_and_assign_codes(parent, code_dict):
    """
    for a given `parent` node, traverse it's children and add the binary representation of the
    leaf nodes to the provided `code_dict`

    binary representation is assigned by treating the left child as 0 and the right child as 1

    :param HuffmanNode parent: the parent node whose children we will traverse
    :param dict code_dict: a dictionary of running code assignments

    for ex, the following binary tree:
         dec
         / \
        /   \
       de     c
      / \
     d   e

    would correspond to the following binary representations:
          .
         / \
        /   \
       0     1
      / \
     00  01

    and would produce this code assignment for its leaves:
    {
        'd': '00',
        'e': '01',
        'c': '1',
    }
    """
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

    # compare nodes by frequency
    if node_q_1.peak()[1] < node_q_2.peak()[1]:
        return node_q_1.dequeue()
    else:
        return node_q_2.dequeue()


class HuffmanNode:
    def __init__(self, label='', left_child=None, right_child=None, binary_code=''):
        self.label = label
        self.left_child = left_child
        self.right_child = right_child
        self.binary_code = binary_code

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