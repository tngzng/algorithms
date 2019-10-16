import unittest

from algorithms.union_find import UnionFind, Node


class TestUnionFind(unittest.TestCase):
    def test_find(self):
        """
        model a graph with two partitions:
        a <- b <- c

        d <- e
        """
        test_union_find = UnionFind()
        # override internal data structure to setup test
        test_union_find._union_find = {
            'c': Node('c', parent_label='b', rank=0),
            'b': Node('b', parent_label='a', rank=1),
            'a': Node('a', parent_label='a', rank=2),
            'e': Node('e', parent_label='d', rank=0),
            'd': Node('d', parent_label='d', rank=1),
        }
        expected_leaders = [
            ('c', 'a'),
            ('b', 'a'),
            ('a', 'a'),
            ('e', 'd'),
            ('d', 'd'),
        ]
        for child, expected_leader in expected_leaders:
            self.assertEqual(test_union_find.find(child), expected_leader)

    def test_find__compresses_path_to_leader(self):
        """
        model a graph with one partition:
        a <- b <- c <- d
        """
        test_union_find = UnionFind()
        # override internal data structure to setup test
        test_union_find._union_find = {
            'd': Node('d', parent_label='c', rank=1),
            'c': Node('c', parent_label='b', rank=1),
            'b': Node('b', parent_label='a', rank=2),
            'a': Node('a', parent_label='a', rank=3),
        }
        test_union_find.find('d')
        for child_label in ['d', 'c', 'b']:
            child_node = test_union_find._union_find[child_label]
            self.assertEqual(child_node.parent_label, 'a')

    def test_union__leaders_have_diff_ranks(self):
        """
        model a graph with two partitions:
        a <- b <- c

        d <- e
        """
        test_union_find = UnionFind()
        # override internal data structure to setup test
        test_union_find._union_find = {
            'c': Node('c', parent_label='b', rank=0),
            'b': Node('b', parent_label='a', rank=1),
            'a': Node('a', parent_label='a', rank=2),
            'e': Node('e', parent_label='d', rank=0),
            'd': Node('d', parent_label='d', rank=1),
        }
        test_union_find.union('c', 'e')

        smaller_ranked_leader = test_union_find._union_find['d']
        larger_ranked_leader = test_union_find._union_find['a']

        self.assertEqual(smaller_ranked_leader.parent_label, larger_ranked_leader.label)

    def test_union__leaders_have_same_ranks(self):
        """
        model a graph with two partitions:
        a <- b <- c

        d <- e
        """
        test_union_find = UnionFind()
        # override internal data structure to setup test
        test_union_find._union_find = {
            'b': Node('b', parent_label='a', rank=0),
            'a': Node('a', parent_label='a', rank=1),
            'e': Node('e', parent_label='d', rank=0),
            'd': Node('d', parent_label='d', rank=1),
        }
        test_union_find.union('b', 'e')

        leader_1 = test_union_find._union_find['d']
        leader_2 = test_union_find._union_find['a']

        # figure out which leader has become the new child and new parent
        child = leader_1 if leader_1.parent_label != leader_1.label else leader_2
        parent_leader = leader_1 if leader_1.parent_label == leader_1.label else leader_2

        self.assertEqual(child.parent_label, parent_leader.label)
        # the new parent's rank should have gone up by 1
        self.assertEqual(parent_leader.rank, 2)
