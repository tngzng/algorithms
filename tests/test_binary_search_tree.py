import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '../..'))
import unittest
from binary_search_tree import BinarySearchTree

class TestHeap(unittest.TestCase):
    def test_insert(self):
        bst = BinarySearchTree()
        root = bst.insert(4)
        self.assertEqual(bst.root, root)

        left_child = bst.insert(2)
        self.assertEqual(bst.root.left_child, left_child)
        left_child_left_child = bst.insert(1)
        self.assertEqual(bst.root.left_child.left_child, left_child_left_child)
        left_child_right_child =bst.insert(3)
        self.assertEqual(bst.root.left_child.right_child, left_child_right_child)

        right_child = bst.insert(6)
        self.assertEqual(bst.root.right_child, right_child)
        right_child_left_child = bst.insert(5)
        self.assertEqual(bst.root.right_child.left_child, right_child_left_child)
        right_child_right_child = bst.insert(7)
        self.assertEqual(bst.root.right_child.right_child, right_child_right_child)

