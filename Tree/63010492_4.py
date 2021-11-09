class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            curr = self.root
            while True:
                if data < curr.data:
                    if curr.left == None:
                        curr.left = Node(data)
                        break
                    curr = curr.left
                else:
                    if curr.right == None:
                        curr.right = Node(data)
                        break
                    curr = curr.right
        return self.root
    def delete(self, r, data):
        if r is None:  # base case
            print("Error! Not Found DATA")
            return
        if r.data != data:  # not found

            if r.data > data:
                r.left = self.delete(r.left, data)  # not found left
            elif r.data < data:
                r.right = self.delete(r.right, data)  # not found right



        else:  # found !!!!

            if r.left is None:  # left None
                node = r.right
                return node
            elif r.right is None:  # right None
                node = r.left
                return node
            else:
                current = r.right
                while current.left is not None:
                    current = current.left

                r.data = current.data  # replace delete
                r.right = self.delete(r.right, current.data)  # permanent delete recursive.....

        return r
    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)\

T = BST()
data = input("Enter Input : ").split(",")
for i in range(len(data)):
    data[i] = data[i].split()
    if data[i][0] == 'd':
        print("delete " + (data[i][1]))
        T.root = T.delete(T.root, int(data[i][1]))
        T.printTree(T.root)
    elif data[i][0] == 'i':
        print("insert " + (data[i][1]))
        T.insert(int(data[i][1]))
        T.printTree(T.root)