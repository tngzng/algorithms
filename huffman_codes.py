from typing import List, Tuple, Dict, Any


class HuffmanNode:
    def __init__(self, label: str = '', left_child: 'HuffmanNode' = None,
                 right_child: 'HuffmanNode' = None, binary_code: str = '') -> None:
        self.label = label
        self.left_child = left_child
        self.right_child = right_child
        self.binary_code = binary_code

    def update_left_child(self, left_child: 'HuffmanNode') -> None:
        self.left_child = left_child

    def update_right_child(self, right_child: 'HuffmanNode') -> None:
        self.right_child = right_child

    def update_code(self, binary_code: str) -> None:
        self.binary_code = binary_code

    def update_label(self, label: str) -> None:
        self.label = label

    def __repr__(self) -> str:
        return self.label


class Queue:
    def __init__(self) -> None:
        self._queue = []

    def peak(self) -> Any:
        return self._queue[-1]

    def enqueue(self, el: Any) -> None:
        self._queue.insert(0, el)

    def dequeue(self) -> Any:
        return self._queue.pop()

    def __len__(self) -> int:
        return len(self._queue)

    def __str__(self) -> str:
        return self._queue.__str__()

    def __repr__(self) -> str:
        return self._queue.__repr__()

    
def huffman_codes(char_frequencies: List[Tuple[str, int]]) -> Dict[str, int]:
    """
    given an alphabet where each character has a different frequency of occurring,
    produce a representation in binary for each character that minimizes the memory
    needed to encode something in the alphabet

    we do this by constructing a binary tree out of the chars in the alphabet,
    where the lowest frequency chars have the largest depths from the root
    and the highest frequency chars have the lowest depths from the root.

    this allows us to output a binary representation of each char given its position in the tree
    that is smaller for high frequency chars and larger for low frequency chars,
    providing overall memory savings

    :param (list) char_frequencies: a list of tuples representing chars and their frequencies
    :returns (dict): a dict representing chars and their binary encodings

    for ex, for the following char_frequencies:
    [
        ('c', 1),
        ('a', 5),
        ('t', 1),
    ]

    because 'a' occurs more than 'c' or 't', it should have the smallest encoding length

    the final encodings output might look like:
    {
        'c': '00',
        'a': '1',
        't': '01',
    }
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
        # since we build the tree from bottom to top that means
        # the highest frequency chars will end up near the root of the tree where we want them
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
            parent_label = f'{parent_label}{right_node.label}'

        parent_node.update_label(parent_label)

        # break when the binary tree has been fully constructed
        if not len(subtree_q) and not len(node_q):
            break

        subtree_q.enqueue((parent_node, combined_frequency))

    code_dict = {}
    _traverse_children_and_assign_codes(parent_node, code_dict)
    return code_dict


def _traverse_children_and_assign_codes(parent: HuffmanNode, code_dict: Dict[str, int]) -> None:
    """
    for a given `parent` node, traverse its children and add the binary representation of the
    leaf nodes to the provided `code_dict`

    binary representation is assigned by treating the left child as 0 and the right child as 1

    :param (HuffmanNode) parent: the parent node whose children we will traverse
    :param (dict) code_dict: a dictionary of running code assignments

    for ex, the following binary tree:
         cta
         / \
        /   \
       ct     a
      / \
     c   t

    would correspond to the following binary representations:
          .
         / \
        /   \
       0     1
      / \
     00  01

    and would produce this code assignment for its leaves:
    {
        'c': '00',
        't': '01',
        'a': '1',
    }
    """
    # when we hit a leaf, add its binary code to our final output dict
    if not parent.left_child and not parent.right_child:
        code_dict[parent.label] = parent.binary_code

    # TODO: update to return codes as a bitarray for memory savings
    if parent.left_child:
        left_code = f'{parent.binary_code}0'
        parent.left_child.update_code(left_code)
        _traverse_children_and_assign_codes(parent.left_child, code_dict)

    if parent.right_child:
        right_code = f'{parent.binary_code}1'
        parent.right_child.update_code(right_code)
        _traverse_children_and_assign_codes(parent.right_child, code_dict)


def _compare_and_pop_smallest(node_q_1: Queue, node_q_2: Queue) -> HuffmanNode:
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
