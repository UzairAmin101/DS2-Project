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

    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None
        self.dist = 0

    def update_dist(self):
        if self.right == None or self.left == None:
            self.dist = 0
        else:
            self.dist = min(self.right.dist, self.left.dist) + 1


class skewHeap:

    def __init__(self, leftist) -> None:
        self.root = None
        self.size = 0
        self.leftist = leftist

    def insert(self, key):
        x = skewNode(key)
        self.size += 1
        self.root = self.merge(self.root, x)

    def get_min(self):
        return self.root.value

    def extract_min(self):
        x = self.root.value
        self.root = self.merge(self.root.left, self.root.right)
        return x

    def npl(self, h1):
        pass

    def merge(self, h1, h2):

        if h1 == None:
            return h2
        if h2 == None:
            return h1

        if h2.value < h1.value:
            h2, h1 = h1, h2

        # if not self.leftist:
        h1.left, h1.right = h1.right, h1.left

        h1.left = self.merge(h2, h1.left)
        # if self.leftist:
        #     if h1.dist != 0 and h1.left.dist < h1.right.dist:
        #         h1.left, h1.right = h1.right, h1.left

        return h1


sh = skewHeap(True)
sh.insert(10)
sh.insert(9)
sh.insert(56)
sh.insert(1)
sh.insert(99)
sh.insert(72)
sh.insert(6)

# print(sh.get_min())
# printLevelOrder(sh.root)
# print()
# print(sh.extract_min())
# printLevelOrder(sh.root)

# print(sh.root.value)
# print(sh.root.left.value)
# print(sh.root.left.left.value)
# print(sh.root.left.left.left.value)
# print(sh.root.left.left.left.left.value)
# print(sh.root.right.value)
# print(sh.root.right.left.value)
# print(sh.root.right.right.right.value)


print(sh.root.right.left.left.value)