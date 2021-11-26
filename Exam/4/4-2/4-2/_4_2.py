class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    
    def __str__(self):
        return str(self.data)

class AVLTree:
    def __init__(self):
        self.root = None

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def insert(self, root, data):
        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        root.height = 1 + max(self.getHeight(root.right), self.getHeight(root.left))
        balance = self.getBalance(root)

        # Left Left 
        if balance > 1 and data < root.left.data: 
            return self.rightRotate(root) 
        # Right Right 
        if balance < -1 and data >= root.right.data: 
            return self.leftRotate(root) 

        # Left Right 
        if balance > 1 and data >= root.left.data: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 

        # Right Left 
        if balance < -1 and data < root.right.data: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 

        return root

    def leftRotate(self, z): 
        y = z.right 
        temp = y.left 
        y.left = z 
        z.right = temp
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right)) 
        return y 

    def rightRotate(self, z): 
        y = z.left 
        temp = y.right 
        y.right = z 
        z.left = temp 
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right)) 
        return y 

    def getHeight(self, root): 
        if not root: 
            return 0
        return root.height 

    def getBalance(self, root): 
        if not root: 
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def print_preorder(self, node=-1):
        if node == -1:
            node = self.root
        if node != None:
            print(node.data, end=" ")
            self.print_preorder(node.left)
            self.print_preorder(node.right)

    def print_inorder(self, node=-1):
        if node == -1:
            node = self.root
        if node != None:
            self.print_inorder(node.left)
            print(node.data, end=" ")
            self.print_inorder(node.right)

    def print_postorder(self, node=-1):
        if node == -1:
            node = self.root
        if node != None:
            self.print_postorder(node.left)
            self.print_postorder(node.right)
            print(node.data, end=" ") 


print(" *** AVL Tree ***")    
input_string = input("Enter some numbers : ")
root = None
bst = AVLTree()
for n in input_string.split():
	root = bst.insert(root, n)
print("in_order  --> ", end=''); 
bst.print_inorder(root); 
print();
print("preorder  --> ", end=''); 
bst.print_preorder(root); 
print()
print("postorder --> ", end='');
bst.print_postorder(root); 
print();