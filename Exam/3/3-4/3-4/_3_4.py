class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            curr = self.root
            while True:
                if data < curr.data:
                    if curr.left is None:
                        curr.left = Node(data)
                        break
                    curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = Node(data)
                        break
                    curr = curr.right
        return self.root


def height(obj):
    if not obj:
        return -1
    left = height(obj.left) + 1
    right = height(obj.right) + 1
    return max(left, right)

print(" *** Binary Search Tree Height ***")
tree = BinarySearchTree()
arr = list(map(int, input("Enter Input : ").split()))
for e in arr:
     tree.create(e)

print("Height = ",height(tree.root),end="\n\n")