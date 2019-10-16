import unittest

from algorithms.binary_search_tree import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):
    def test_insert(self):
        """
        test the following binary search tree
              4
             / \
            /   \
           2     6
          / \   / \
         1   3  5  7
        """
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
        test the following binary search tree
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
        test the following binary search tree
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

    def test_prev_node_has_left_subtree(self):
        """
        test the following binary search tree
             4 <-- get prev node of 4
            /
           2
          / \
         1   3
        """
        bst = BinarySearchTree()
        node = bst.insert(4)
        bst.insert(2)
        bst.insert(1)
        expected_prev = bst.insert(3)
        self.assertEqual(bst.prev(node), expected_prev)

    def test_prev_node_has_no_left_subtree(self):
        """
        test the following binary search tree
             4
            /
           1
            \
             3
            /
           2 <-- get prev node of 2
        """
        bst = BinarySearchTree()
        bst.insert(4)
        expected_prev = bst.insert(1)
        bst.insert(3)
        node = bst.insert(2)
        self.assertEqual(bst.prev(node), expected_prev)

    def test_prev_node_of_min(self):
        """
        test the following binary search tree
             3
            /
           2
          /
         1 <-- get prev node of 1
        """
        bst = BinarySearchTree()
        bst.insert(3)
        bst.insert(2)
        node = bst.insert(1)
        self.assertEqual(bst.prev(node), None)

    def test_next_node_has_right_subtree(self):
        """
        test the following binary search tree
         1 <-- get next node of 1
          \
           3
          / \
         2   4
        """
        bst = BinarySearchTree()
        node = bst.insert(1)
        bst.insert(3)
        expected_next = bst.insert(2)
        bst.insert(4)
        self.assertEqual(bst.next(node), expected_next)

    def test_next_node_has_no_right_subtree(self):
        """
        test the following binary search tree
             4
            /
           1
            \
             2
              \
               3 <-- get next node of 3
        """
        bst = BinarySearchTree()
        expected_next = bst.insert(4)
        bst.insert(1)
        bst.insert(2)
        node = bst.insert(3)
        self.assertEqual(bst.next(node), expected_next)

    def test_prev_node_of_min(self):
        """
        test the following binary search tree
         1
          \
           2
            \
             3 <-- get next node of 3
        """
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(2)
        node = bst.insert(3)
        self.assertEqual(bst.next(node), None)

    def test_traverse_in_order(self):
        """
        test the following binary search tree
              4
             / \
            /   \
           2     6
          / \   / \
         1   3  5  7
        """
        bst = BinarySearchTree()
        node_4 = bst.insert(4)
        node_2 = bst.insert(2)
        node_1 = bst.insert(1)
        node_3 = bst.insert(3)
        node_6 = bst.insert(6)
        node_5 = bst.insert(5)
        node_7 = bst.insert(7)
        ordered_tree = bst.traverse_in_order()
        expected = [node_1, node_2, node_3, node_4, node_5, node_6, node_7]
        self.assertTrue(all(a == b for a, b in zip(ordered_tree, expected)))
