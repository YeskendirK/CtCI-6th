class RankNode:
    def __init__(self, value = 0):
        self.left_size = 0
        self.left, self.right = None, None
        self.val = value

    def insert(self, d):
        if d <= self.val:
            if self.left is not None:
                self.left.insert(d)
            else:
                self.left = RankNode(d)
            self.left_size += 1
        else:
            if self.right is not None:
                self.right.insert(d)
            else:
                self.right = RankNode(d)

    def get_rank(self, d):
        if d == self.val:
            return self.left_size
        elif d < self.val:
            if self.left is None:
                return -1
            else:
                self.left.get_rank(d)
        else:
            right_rank = -1 if self.right is None else self.right.get_rank(d)
            if right_rank == -1:
                return -1
            else:
                return self.left_size + 1 + right_rank
    def track(self, num):
        if self is None:
            self = RankNode(num)
        else:
            self.insert(num)




