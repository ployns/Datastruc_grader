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
    
    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)\

    def in_order(self, node):
        if node == None:
            return ''

        s = self.in_order(node.left)\
             + str(node.data) + ' '\
                 + self.in_order(node.right)
        return s

    def pre_order(self, node):
        if node == None:
            return ''

        s = str(node.data) + ' '\
            + self.pre_order(node.left)\
                + self.pre_order(node.right)
        return s

    def post_order(self, node):
        if node == None:
            return ''
        
        s = self.post_order(node.left)\
            + self.post_order(node.right)\
                + str(node.data) + ' '
        return s

    def Below(self, node, data):
        if node == None:
            return ''
        
        ans = self.Below(node.left, data)
        if int(node.data) < int(data):
            ans = ans + str(node.data) + ' '
        ans += self.Below(node.right, data)

        return ans

T = BST()
inp, k = input('Enter Input : ').split('|')
inp = [int(i) for i in inp.split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
temp = T.Below(root,k)
print('--------------------------------------------------')
print('Below',k,':',temp if temp != '' else 'Not have')
