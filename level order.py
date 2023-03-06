def printCurrentLevel(root, i):
    pass


class Node:
    def __init__(self,key):
        self.data = key
        self.right = None
        self.left = None

#functiom to print level order traversal of tree
    def printLevelorder(root, level):
        h = root.height(root)
      for i in range(1, h+1):
          printCurrentLevel(root, i)

    def printCurrentLevel(root, level):
        if root is None:
            return
        if level == 1:
            print(root.data, end="")
        elif level > 1:
            printCurrentLevel(root.left, level-1)
            printCurrentLevel(root.right, level-1)

    def height(node, root):
        if node is None:
            return
        else:
            lheight = node.height(node.left)
            rheight = node.height(node.right)
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

root = Node (1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node (4)
root.left.right = Node (5)
print
'/n level order traversal in binary tree is -1'


def printLevelorder(root):
    pass


printLevelorder(root)


