from collections.abc import Iterable
from queue import Queue_List
from stack import Stack_List

class N_Ary_Node:
    def __init__(self, value = None, children = None):
        '''
        Constructor for n-ary node
        '''
        if not isinstance(children, (Iterable, type(None))):
            raise ValueError("The children provided should be an instance of Iterable")
        self.value = value 
        self. children = children if children else []
    def __str__(self):
        return str(self.value)

class CommonTreeMethods:
    '''
    Common n-ary tree utility
    '''
    def __init__(self, value = None, n = 3):
        '''
        Constructor to initialize n-ary tree
        '''
        if not isinstance(n,int):
            raise ValueError(' `n` value should be an integer only')
        self.root = None
        self.n = n
        self.numOfNodes = 0
        if value is not None:
            self.root = self.make_node(value)
            self.numOfNodes = 1
        
    def create_root_if_none(self, value):
        '''
        function to create root if it is None
        '''
        if self.root is None:
            self.root = self.make_node(value)
            return True
        return False

    def make_node(self, value):
        '''
        Creates an N-ary Node with `value` 
        '''
        if  isinstance(value, N_Ary_Node):
            return value
        if value is None:
            raise ValueError("Cannot insert NoneType to the tree")
        return N_Ary_Node(value)

    def check_remove_root(self):
        '''
        helper function to check if the root is none,
        or if the root is the only element in the tree,
        if so, removes the root.
        '''
        if self.root is None:
            return True
        if not self.root.children:
            self.root = None
            self.numOfNodes -= 1
            return True
        return False

    def empty(self):
        '''
        Checks if the tree is empty
        '''
        return self.root is None

    def preorder(self, node = None, fn = print):
        '''
        Preorder traversal of tree
        '''
        if self.empty():
            return
        if node is None:
            node = self.root
        stack = Stack_List()
        stack.insert(self.root)
        while not stack.empty():
            node = stack.remove()
            
            fn(node.value)

            for child in reversed(node.children):
                stack.insert(child)

    def topological_sort(self):
        '''
        returns iterable containing all elements sorted in topologically
        '''
        sortedElements = []
        self.preorder(fn = lambda x: sortedElements.append(x))
        return sortedElements
        

    def levelorder(self, node = None, fn = print):
        '''
        Level order traversal of tree
        '''
        if self.empty():
            return
        if node is None:
            node = self.root
        queue = Queue_List()
        queue.insert(self.root)
        while not queue.empty():
            node = queue.remove()
            fn(node.value)
            for child in node.children:
                queue.insert(child)

    def dfs(self, value):
        '''
        Finds an element using dfs, returns True if found else returns False
        '''
        found = False
        if self.empty():
            return found
        stack = Stack_List()
        stack.insert(self.root)
        while not stack.empty():
            node = stack.remove()

            if node.value == value:
                found = True
                break

            for child in reversed(node.children):
                stack.insert(child)
        return found


    def bfs(self, value):
        '''
        Finds an element using bfs, returns True if found else returns False
        '''
        found = False
        if self.empty():
            return found
        queue = Queue_List()
        queue.insert(self.root)
        while not queue.empty():
            node = queue.remove()

            if node.value == value:
                found = True
                break

            for child in reversed(node.children):
                queue.insert(child)
        return found
        

class Tree(CommonTreeMethods):
    '''
    Generic N-Ary Tree
    '''

    def insert(self, value):
        '''
        inserts an element to the tree in level - order fashion
        '''
        if self.create_root_if_none(value):
            return
        queue = Queue_List()    
        queue.insert(self.root)
        self.numOfNodes += 1
        while not queue.empty():
            node = queue.remove()
            if len(node.children) < self.n:
                node.children.append(self.make_node(value))
                break
            for child in node.children:
                queue.insert(child)
        
        