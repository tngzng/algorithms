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

    def test_min(self):
        """
        test the min from the following binary search tree
             3
            /
           2
          /
         1
        """
        bst = BinarySearchTree()
        bst.insert(3)
        bst.insert(2)
        expected_min = bst.insert(1)
        self.assertEqual(bst.min(), expected_min)

    def test_max(self):
        """
        test the max from the following binary search tree
         1
          \
           2
            \
             3
        """
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(2)
        expected_max = bst.insert(3)
        self.assertEqual(bst.max(), expected_max)
