from Stack import Stack


class StackMin():
    def __init__(self):
        self.items = []
        self.min = None

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if self.min is None:
            self.min = item
        elif self.min and item < self.min:
            self.min = item
        self.items.append(item)

    def pop(self):
        self.items.pop()
        self.min = self.items[0]
        for element in self.items:
            if element < self.min:
                self.min = element

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def stack_min(self):
        return self.min


# Solution 2
class StackMin_2():
    def __init__(self):
        self.items = []
        self.min_values = Stack()

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if self.min_values.isEmpty():
            self.min_values.push(item)
        elif not self.min_values.isEmpty() and item <= self.min_values.peek():
            self.min_values.push(item)
        self.items.append(item)

    def pop(self):
        if self.min_values.peek() and self.items[-1] == self.min_values.peek():
            self.min_values.pop()
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def stack_min(self):
        return self.min_values.peek()


stack1 = StackMin()
stack1.push(3)
stack1.push(4)
stack1.push(5)
stack1.push(1)
# print(stack1.items)
stack1.pop()
# print(stack1.items)
# print(stack1.stack_min())

stack2 = StackMin_2()
stack2.push(3)
stack2.push(4)
stack2.push(5)
stack2.push(1)
print(stack2.items)
stack2.pop()
print(stack2.items)
print(stack2.stack_min())
