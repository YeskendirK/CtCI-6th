class Node(object):
    def __init__(self, value):
        self.value = value
        self.above = None
        self.below = None


class Stack(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.top = None
        self.bottom = None

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def join(self, above, below):
        if below:
            below.above = above
        if above:
            above.below = below

    def push(self, item):
        if self.size >= self.capacity:
            return False
        self.size += 1
        node = Node(item)
        if self.size == 1:
            self.bottom = node
        self.join(node, self.top)
        self.top = node
        return True

    def pop(self):
        if not self.top:
            return None
        node = self.top
        self.top = self.top.below
        self.size -= 1
        return node.value

    def remove_bottom(self):
        b = self.bottom
        self.bottom = self.bottom.above
        if self.bottom:
            self.bottom.below = None
        self.size -= 1
        return b.value


class SetOfStacks(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def get_last_stack(self):
        if not self.stacks:
            return None
        return self.stacks[-1]

    def isEmpty(self):
        last = self.get_last_stack()
        return not last or last.isEmpty()

    def push(self, item):
        last = self.get_last_stack()
        if last and not last.isFull():
            last.push(item)
        else:
            stack = Stack(self.capacity)
            stack.push(item)
            self.stacks.append(stack)

    def pop(self):
        last = self.get_last_stack()
        if not last:
            return None
        item = last.pop()
        if last.size == 0:
            del self.stacks[-1]
        return item

    def pop_at(self, index):
        return self.leftShift(index, True)

    def leftShift(self, index, remove_top):
        stack = self.stacks[index]
        removed_item = stack.pop() if remove_top else stack.remove_bottom()
        if stack.isEmpty():
            del self.stacks[index]
        elif len(self.stacks) > index + 1:
            v = self.leftShift(index + 1, False)
            stack.push(v)
        return removed_item


