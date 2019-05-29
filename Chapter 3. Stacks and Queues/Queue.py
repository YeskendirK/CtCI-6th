class Queue():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.itmes == []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
