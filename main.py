from classes.my_classes import Leaf, Operations

root = Leaf(5)
root.left = Leaf(3)
root.right = Leaf(7)
root.left.left = Leaf(2)
root.left.right = Leaf(5)
root.right.left = Leaf(1)
root.right.right = Leaf(0)
root.right.right.right = Leaf(8)
root.right.right.right.right = Leaf(5)
 
x = Operations(root)
x.sum_all_leaves(root)
x.num_of_leaves(root)
x.mean_tree(root)
x.median_tree(root)
x.sum_of_children(root)
print("Sum of children for every parent: ")
x.print_inorder(root)





