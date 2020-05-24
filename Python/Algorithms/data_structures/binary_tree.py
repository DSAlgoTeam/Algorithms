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

class CommonTreeMethods:
    '''
    Generic Tree Utility
    '''
    def __init__(self, value=None):
        '''
        Constructor to initialize a Tree.
        '''
        self.root = None
        self.height = 0
        self.numOfNodes = 0
        if value is not None:
            self.root = self.make_node(value)
            self.length = 1
            self.height = 1
    
    def create_root_if_none(self,value):
        if self.root is None:
            self.root = self.make_node(value)
            self.height += 1
            self.length += 1
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
        if self.root.next is None:
            self.root = None
            self.length -= 1
            return True

        return False
    
    def inorder(self, node = None, fn = print):
        '''
        returns an iterable containing all the elements after inorder traversal

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
        returns an iterable containing all the elements after preorder traversal

        '''
        if node is None:
            node = self.root
        
        fn(node.value)
        if node.left:
            self.inorder(node.left,fn)
        if node.right:
            self.inorder(node.right,fn)
    
    def postorder(self, node = None, fn = print):
        '''
        returns an iterable containing all the elements after preorder traversal

        '''
        if node is None:
            node = self.root
        
        if node.left:
            self.inorder(node.left,fn)

        if node.right:
            self.inorder(node.right,fn)

        fn(node.value)
    

    def dfs(self, v):
        '''
        
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




    def __len__(self):
        return self.length
    
    # TODO: finish implementation of __str__
    #def __str__(self):
        # TODO: figure out the string representation


class Tree(CommonTreeMethods,Abstract_Tree):
    def insert(self,value):
        print('')

class TreeNode:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right