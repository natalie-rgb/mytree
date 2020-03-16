import unittest
from classes.Operation import Operations
from classes.Operation import Leaf


class TestTree(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

    def setUp(self):
        self.tree = Operations()
        self.tree.root = Leaf(5)
        self.tree.root.left = Leaf(3)
        self.tree.root.right = Leaf(7)
        self.tree.root.left.left = Leaf(2)
        self.tree.root.left.right = Leaf(5)
        self.tree.root.right.left = Leaf(1)
        self.tree.root.right.right = Leaf(0)
        self.tree.root.right.right.right = Leaf(8)
        self.tree.root.right.right.right.right = Leaf(5)

    def test_size_correct(self):
        self.assertEqual(self.tree.num_of_leaves(self.tree.get_root()), 9)

    def test_mean_correct(self):
        self.assertEqual(self.tree.mean_tree(self.tree.get_root()), 4.0)

    def test_median_correct(self):
        self.assertEqual(self.tree.median_tree(self.tree.get_root()), 5)

    def test_root_is_none(self):
        self.assertEqual(self.tree.median_tree(None), 0)
        self.assertEqual(self.tree.sum_all_leaves(None), 0)
        self.assertEqual(self.tree.sum_of_children(None), 0)
        self.assertEqual(self.tree.print_inorder(None), 0)
        self.assertEqual(self.tree.num_of_leaves(None), 0)


if __name__ == '__main__':
    unittest.main()




