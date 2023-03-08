class Node:

    def __init__(self,data):
        self.data = key
        self.left = None
        self.right = None

    def maxDepth(Node):
        if node is None:
            return 0
        else:
            lDepth = maxDepth(node.left)
            rDepth = maxDepth(node.right)

            #use the larger one
            if(lDepth > rDepth):
                return lDepth+1
            else:
                return rDepth+1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Height of a tree is %" %(maxDepth(root)))
