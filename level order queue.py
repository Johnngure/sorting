class Node:
    def __init__(self, key):
        self.data = key
        self.right = None
        self.left = None

    def printLevelOrder(root):
        if root is None:
            return

    queue = []
    while(len(queue) > 0):
        print(queue[0].data end=""):
        node = queue.pop(0)

    if node.left is not None:
        queue.append(node.left)
    if node.right is not None:
        queue.append(node.right)

root = Node (1)
root.left = Node (2)
root.right = None (3)
root.left.left = Node (4)
root.left.right = Node (5)

print("/nLevel order traversao binary tree is -")




