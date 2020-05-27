from abc import ABCMeta,abstractmethod
from stack import Stack_List
from queue import Queue_List

class Abstract_Tree(metaclass=ABCMeta):
    '''
    Abstraction of Tree Class
    '''
    @abstractmethod
    def insert(self,value):
        return
    
    # @abstractmethod
    # def remove(self):
    #     return

class CommonBinaryTreeMethods:
    '''
    Generic Tree Utility
    '''
    def __init__(self, value=None):
        '''
        Constructor to initialize a Tree.
        '''
        self.root = None
        self.numOfNodes = 0
        if value is not None:
            self.root = self.make_node(value)
            self.numOfNodes = 1
    
    def create_root_if_none(self,value):
        if self.root is None:
            self.root = self.make_node(value)
            self.numOfNodes += 1
            return True
        return False
    
    def make_node(self, value):
        if value is None:
            raise ValueError("Nonetype Argument not expected")
        
        return value if isinstance(value, TreeNode) else TreeNode(value)

    def check_remove_root(self):
        '''
        Helper function to check and remove if it has no tree nodes or 1 tree node.
        '''
        if self.root is None:
            return True
        if self.root.left is None and self.root.right is None:
            self.root = None
            self.numOfNodes -= 1
            return True

        return False
    
    def inorder(self, node = None, fn = print):
        '''
        Applies `fn` to all elements during inorder traversal

        '''
        if node is None:
            node = self.root
        if node.left:
            self.inorder(node.left,fn)

        fn(node.value)
        
        if node.right:
            self.inorder(node.right,fn)

    def preorder(self, node = None, fn = print):
        '''
        Applies `fn` to all elements during preorder traversal

        '''
        if node is None:
            node = self.root
        
        fn(node.value)
        if node.left:
            self.preorder(node.left,fn)
        if node.right:
            self.preorder(node.right,fn)
    
    def postorder(self, node = None, fn = print):
        '''
        Applies `fn` to all elements during postorder traversal

        '''
        if node is None:
            node = self.root
        
        if node.left:
            self.postorder(node.left,fn)

        if node.right:
            self.postorder(node.right,fn)

        fn(node.value)
    
    def levelorder(self, node = None, fn = print):
        '''
        Applies `fn` to all elements during level order traversal
        '''
        node = node if node else self.root
        h = self.height(node)
        for i in range(1,h+1):
            self.apply_to_level(node, i, print)

    def apply_to_level(self, node, level, fn = print):
        '''
        Applies given function to a level.
        '''
        if node is None:
            return
        if level == 1:
            fn(node.value)
        if level > 1:
            self.apply_to_level(node.left, level - 1, fn)
            self.apply_to_level(node.right, level - 1, fn)

    
    def height(self, node):
        '''
        find the height of a node in the tree from the bottom most element in that subtree.

        '''
        if node is None:
            return 0
        
        lheight = self.height(node.left)
        rheight = self.height(node.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

    def dfs(self, v):
        '''
        searches for element v using dfs in tree
        '''
        found = False
        stack = Stack_List(self.root)
        while not stack.empty():
            node = stack.remove()
            if node.value == v:
                found = True
                break

            if node.right:
                stack.insert(node.right)
            if node.left:
                stack.insert(node.left)
        return found
    
    def bfs(self, v):
        '''
        searches for element v using bfs in tree
        '''
        found = False
        queue = Queue_List(self.root)
        while not queue.empty():
            node = queue.remove()

            if node.value == v:
                found = True
                break
            
            if node.left:
                queue.insert(node.left)

            if node.right:
                queue.insert(node.right)
        return found

    def topological_sort(self):
        sortedElements = []
        self.preorder(self.root, lambda x: sortedElements.append(x))
        return sortedElements


    def __len__(self):
        return self.numOfNodes
    


class BinaryTree(CommonBinaryTreeMethods,Abstract_Tree):
    def insert(self,value):
        '''
        Level order insertion of nodes
        '''
        if self.create_root_if_none(value):
            return
        queue = Queue_List(self.root)
        self.numOfNodes += 1
        while not queue.empty():
            node = queue.remove()
            if not node.left:
                node.left = self.make_node(value)
                break
            else:
                queue.insert(node.left)
            if not node.right:
                node.right = self.make_node(value)
                break
            else:
                queue.insert(node.right)

class TreeNode:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right