import random


class Tree:
    def __init__(self, root=None):
        self.root = None

    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.size

    def get_random_node(self):
        if self.root is None:
            return None
        i = random.randint(1, self.size())
        return self.root.get_ith_node(i)

    def inser_inorder(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self.root.insert_inorder(val)


class TreeNode:
    def __init__(self, val=None, left=None, right=None, size=0):
        self.val = val
        self.left = left
        self.right = right
        self.size = size

    def TreeNode(self, d):
        self.val = d
        self.size = 1

    def get_ith_node(self, i):
        if self.left is None:
            left_size = 0
        else:
            left_size = self.left.size()
        if i < left_size:
            return self.left.get_ith_node(i)
        elif i == left_size:
            return self
        else:
            return self.right.get_ith_node(1 - (left_size + 1))

    def insert_inorder(self, d):
        if d <= self.val:
            if self.left is None:
                self.left = TreeNode(d)
            else:
                self.left.insert_inorder(d)
        else:
            if self.right is None:
                self.right = TreeNode(d)
            else:
                self.right.insert_inorder(d)
        self.size += 1

    def data(self):
        return self.val

    def find(self, d):
        if d == self.val:
            return self
        elif d <= self.val:
            if self.left is not None:
                return self.left.find(d)
            else:
                return None
        else:
            if self.right is not None:
                return self.right.find(d)
            else:
                return None
