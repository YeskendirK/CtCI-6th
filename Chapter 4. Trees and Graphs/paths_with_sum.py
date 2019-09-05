class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left, self.right = left, right


# Solution-1: Brute Force (O(N logN))

def countPathsWithSum(root, targetSum):
    if root is None:
        return 0
    pathsFromRoot = countPathsWithSumFromNode(root, targetSum, 0)

    pathsOnLeft = countPathsWithSum(root.left, targetSum)
    pathsOnRight = countPathsWithSum(root.right, targetSum)

    return pathsFromRoot + pathsOnLeft + pathsOnRight


def countPathsWithSumFromNode(node, targetSum, curretnSum):
    if node is None:
        return 0
    curretnSum += node.val
    totalPaths = 0
    if curretnSum == targetSum:
        totalPaths += 1

    totalPaths += countPathsWithSumFromNode(node.left, targetSum, curretnSum)
    totalPaths += countPathsWithSumFromNode(node.right, targetSum, curretnSum)

    return totalPaths


# Solution-2: Optimized (O(N))

def countPathsWithSum(root, targetSum):
    hash_table = {}
    countPaths(root, targetSum, 0, hash_table)


def countPaths(node, targetSum, runningSum, hash_table):
    if node is None:
        return 0
    runningSum += node.val
    if runningSum in hash_table:
        hash_table[runningSum] += 1
    else:
        hash_table[runningSum] = 1
    totalPaths = int(runningSum == targetSum)
    totalPaths += countPaths(node.left, targetSum, runningSum, hash_table)
    totalPaths += countPaths(node.right, targetSum, runningSum, hash_table)
    hash_table[runningSum] -= 1

    return totalPaths
