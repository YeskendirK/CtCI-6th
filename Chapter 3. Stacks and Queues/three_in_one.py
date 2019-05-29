class fixed_MultiStack():

    def __init__(self, stackSize):
        self.numOfStacks = 3
        self.values = [0] * (self.numOfStacks * stackSize)
        self.sizes = [0] * self.numOfStacks
        self.stackCapacity = stackSize

    def push(self, item, stackNum):
        if self.isFull(stackNum):
            raise Exception('Stack is full')
        self.sizes[stackNum] += 1
        self.values[self.indexOfTop(stackNum)] = item

    def pop(self, stackNum):
        if self.isEmpty(stackNum):
            raise Exception('Stack is empty')
        topIndex = self.indexOfTop(stackNum)
        value = self.values[topIndex]
        self.values[topIndex] = 0
        self.sizes[stackNum] -= 1

        return value

    def peek(self, stackNum):
        if self.isEmpty(stackNum):
            raise Exception('Stack is empty')
        return self.values[self.indexOfTop(stackNum)]

    def indexOfTop(self, stackNum):
        offset = stackNum * self.stackCapacity
        size = self.sizes[stackNum]
        return offset + size - 1

    def isFull(self, stackNum):
        return self.sizes[stackNum] == self.stackCapacity

    def isEmpty(self, stackNum):
        return self.sizes[stackNum] == 0



def ThreeInOne():
    newstack = fixed_MultiStack(3)
    print(newstack.isEmpty(1))
    newstack.push(3, 1)
    print(newstack.peek(1))
    print(newstack.isEmpty(1))
    newstack.push(2, 1)
    print(newstack.peek(1))
    print(newstack.pop(1))
    print(newstack.peek(1))
    newstack.push(3, 1)
    newstack.push(4, 0)
    newstack.push(5, 0)
    newstack.push(6, 0)
    print(newstack.values)

ThreeInOne()
