from abc import ABCMeta,abstractmethod

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