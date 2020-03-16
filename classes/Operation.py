class Leaf:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class Operations:

    def __init__(self, root = None):
        self.root = root

    def get_root(self):
        return self.root

    def sum_of_children(self, root):
        if root is None:
            return 0
        prev_data = root.data
        root.data = self.sum_of_children(root.left) + self.sum_of_children(root.right)
        return root.data + prev_data

    def print_inorder(self,root):
        if root is None:
            return 0
        self.print_inorder(root.left)
        print(root.data, end=" ")
        self.print_inorder(root.right)

    def sum_all_leaves(self, root):
        global result
        if root is None:
            return 0
        else:
            result += root.data
        self.sum_all_leaves(root.left)
        self.sum_all_leaves(root.right)
        return result

    def num_of_leaves(self, root):
        global num
        if root is None:
            return 0
        else:
            num = (1 + self.num_of_leaves(root.left) + self.num_of_leaves(root.right))
        return num

    def mean_tree(self,root):
        print("Mean of Tree:", result / num)
        return result / num

    def t_inorder(self, root, inorder):
        if root is None:
            return 0
        self.t_inorder(root.left, inorder)
        inorder.append(root.data)
        self.t_inorder(root.right, inorder)

    def median_tree(self, root):
        if root is None:
            return 0
        array = []
        self.t_inorder(root, array)
        array = sorted(array)

        if num % 2 == 0:
            res = array[num // 2 - 1] + array[num // 2]
            print("Median of Tree:", res / 2)
            return res/2
        else:
            print("Median of Tree:", array[num // 2])
            return array[num // 2]

result = 0