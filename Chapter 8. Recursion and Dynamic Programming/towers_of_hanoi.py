class Tower():
    def __init__(self):
        self.disks = []

    def is_empty(self):
        return self.disks == []

    def push(self, item):
        self.disks.append(item)

    def pop(self):
        return self.disks.pop()

    def move_to_top(self, t):
        disk = self.pop()
        t.push(disk)

    def move_disks(self, n, destination, buffer):
        if n > 0:
            self.move_disks(n - 1, buffer, destination)
            self.move_to_top(destination)
            buffer.move_disks(n - 1, destination, buffer)


def towers_of_hanoi(n):
    towers = []
    for i in range(3):
        towers.append(Tower())

    i = n - 1
    while i >= 0:
        towers[0].push(i)
        i -= 1
    print(towers[0].disks)
    print(towers[1].disks)
    print(towers[2].disks)
    towers[0].move_disks(n, towers[2], towers[1])
    print('---------------')
    print(towers[0].disks)
    print(towers[1].disks)
    print(towers[2].disks)
    return

towers_of_hanoi(5)