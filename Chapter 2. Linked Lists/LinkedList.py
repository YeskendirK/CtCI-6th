from random import randint


class Node:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def __set__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.nextNode

    def __str__(self):
        data = [str(x.data) for x in self]
        return '->'.join(data)

    def __len__(self):
        out = 0
        node = self.head
        while node:
            out += 1
            node = node.nextNode
        return out

    def add(self, data):
        if self.head is None:
            self.head = self.tail = Node(data)
        else:
            self.tail.nextNode = Node(data)
            self.tail = self.tail.nextNode
        return self.tail

    def add_to_beginning(self, data):
        if self.head is None:
            self.head = self.tail = Node(data)
        else:
            self.head = Node(data, self.head)
        return self.head

    def generate(self, n, min_value, max_value):
        self.head = self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self
