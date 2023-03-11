class Node:
    def __init__(self,key):
        self.data = key
        self.right = None
        self.left = None

    def insert(node, key):
        if node is None:
            return node (key)
        if key < node.key:
            node.left = node.insert(node.left, key)
        elif key > node.key:
            node.right = node.insert(node.right, key)

        return node
    def inorder(root):
        if root is not None:
            root.inorder(root.left)
            print(root.key, end= "")
            root.inorder(root.right)


def inorder(root):
    pass


def insert(root, param):
    pass


if __name__ == '__main__':
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    
    inorder(root)
    
        


