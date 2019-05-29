from Stack import Stack


class MyQueue():
    def __init__(self):
        self.stack_new = Stack()
        self.stack_old = Stack()

    def size(self):
        return self.stack_new.size() + self.stack_old.size()

    def enqueue(self, item):
        self.stack_new.push(item)

    def shift_stacks(self):
        if self.stack_old.isEmpty():
            while not self.stack_new.isEmpty():
                self.stack_old.push(self.stack_new.pop())

    def peek(self):
        self.shift_stacks()
        return self.stack_old.peek()

    def dequeue(self):
        self.shift_stacks()
        return self.stack_old.pop()


q = MyQueue()
out = []
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.peek())
out.append(q.dequeue())
q.enqueue(4)
q.enqueue(5)
while q.size():
    out.append(q.dequeue())
print(out)
