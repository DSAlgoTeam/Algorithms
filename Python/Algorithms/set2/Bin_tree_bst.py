from abc import ABCMeta, abstractmethod


@abstractmethod
def insert(self, val):
    return


class Tree:

    def __init__(self, val= None):
        if val:
            self.val = val
            self.left = None
            self.right = None

        
class Basic(metaclass=ABCMeta):

    def __init__(self, val=None):

        self.root = None
        if val:
            self.root = Tree(val)


    def preOrder(self, node):
        if not node:
            return
        print(node.val)
        self.preOrder(node.left)
        self.preOrder(node.right)

    def postOrder(self, node):
        if not node:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.val)


    def inOrder(self, node):
        if not node:
            return
        self.inOrder(node.left)
        print(node.val)
        self.inOrder(node.right)


    def topoSort(self, node, arr = []):
        if not node:
            return
        arr.append(node.val)
        self.topoSort(node.left,arr)
        self.topoSort(node.right,arr)

        return arr


    def levelOrderTraverse(self, node = None):
        current = [node]
        while current:
            queue = []
            for i in current:
                print (i.val,end=" ")
                if i.left: queue.append(i.left)
                if i.right: queue.append(i.right)
            print("\n")
            current = queue


    def dfs(self, node = None, key = None) -> bool:
        if not node: return False
        if node.val == key: return True
        return self.dfs(node.left, key) or self.dfs(node.right, key)


    def bfs(self, node, key) -> bool:
        current = [node]
        while current:
            queue = []
            for i in current:
                if i.val == key: return True
                if i.left: queue.append(i.left)
                if i.right: queue.append(i.right)
            current = queue
        return False


    def getHeight(self, node = None):
        if not node: return 0
        return 1 + max(self.getHeight(node.right), self.getHeight(node.left))

        


class Binary_search_tree(Basic):

    def __init__(self, val=None):
        super().__init__(val)


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


class Binary_tree(Basic):

    def __init__(self, val=None):
        super().__init__(val)


    def insert(self, val = None):
        
        current = [self.root]
        while current:
            queue = current.pop(0)

            if not queue.left:
                queue.left = Tree(val)
                break
            else:
                current.append(queue.left)

            if not queue.right:
                queue.right = Tree(val)
                break
            else:
                current.append(queue.right)