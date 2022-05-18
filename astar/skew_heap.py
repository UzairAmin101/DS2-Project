def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printCurrentLevel(root, i)


# Print nodes at a current level
def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.value, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)


""" Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
"""


def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        # Use the larger one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1


# ---------------------------------------------------------------------------------------

class skewNode:

    def __init__(self, priority, data) -> None:
        self.priority = priority
        self.data = data
        self.right = None
        self.left = None
        self.dist = 0

    def update_dist(self):
        if self.right == None or self.left == None:
            self.dist = 0
        else:
            self.dist = min(self.right.dist, self.left.dist) + 1


class skewHeap:

    def __init__(self) -> None:
        self.root = None
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def enqueue(self, priority, data):
        x = skewNode(priority, data)
        self.size += 1
        self.root = self.merge(self.root, x)

    def get_min(self):
        return self.root.data

    def dequeue(self):
        x = self.root.data
        self.size -= 1
        self.root = self.merge(self.root.left, self.root.right)
        return x

    def npl(self, h1):
        pass

    def merge(self, h1, h2):

        if h1 == None:
            return h2
        if h2 == None:
            return h1

        if h2.priority < h1.priority:
            h2, h1 = h1, h2

        h1.left, h1.right = h1.right, h1.left

        h1.left = self.merge(h2, h1.left)

        return h1

    def dfs(self):
        stack = []
        if self.root != None:
            stack.append(self.root)
        visited = []

        while stack:
            x = stack.pop()
            visited.append(x.data)
            if x.left != None:
                stack.append(x.left)
            if x.right != None:
                stack.append(x.right)

        return visited


# sh = skewHeap()
# sh.enqueue(4, 44)
# sh.enqueue(5, 11)
# sh.enqueue(5, 88)
# sh.enqueue(4, 69)
# print(sh.dequeue())
# print(sh.dequeue())
# print(sh.dequeue())
# print(sh.dequeue())
