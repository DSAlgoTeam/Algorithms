from abc import abstractmethod


@abstractmethod
def insert(self, val):
    return
    
class Tree:
    
    def __init__(self, val= None, color = 'R'):
        if val:
            self.val = val
            self.left = None
            self.right = None
            self.color = color



class AVL_tree:

    def __init__(self, val=None):
        super().__init__(val)


    def __init__(self, val = None, color = None):
        self.root = None
        if val:
            self.root = Tree(val)
    
    
    def getHeight(self, node = None):
        if not node: return 0
        return 1 + max(self.getHeight(node.right), self.getHeight(node.left))


    def rotateRight(self, node):
        temp = node.left
        node.left = temp.right
        temp.right = node

        return temp


    def rotateLeft(self, node):
        temp = node.right
        node.right = temp.left
        temp.left = node

        return temp


    def insert(self, val = None):
        if not self.root:
            self.root = Tree(val)
            return

        node = self.root
        while node:
            temp = node
            if val < node.val:
                node = node.left
            else: node = node.right

        if val < temp.val:
            temp.left = Tree(val)
        else: temp.right = Tree(val)

        balance = self.getHeight(self.root.left) - self.getHeight(self.root.right)

        if balance > 1 and val < self.root.left.val:
            self.root = self.rotateRight(self.root)

        elif balance < -1 and val > self.root.right.val: 
            self.root = self.rotateLeft(self.root) 

        elif balance > 1 and val > self.root.left.val: 
            self.root.left = self.leftRotate(self.root.left) 
            self.root = self.rightRotate(self.root) 

        elif balance < -1 and val < self.root.right.val: 
            self.root.right = self.rightRotate(self.root.right) 
            self.root = self.leftRotate(self.root)