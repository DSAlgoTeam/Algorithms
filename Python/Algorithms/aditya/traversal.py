from collections import deque
class Traversal:
    @staticmethod
    def inorder( root ,l): 
  
        if root is not None: 
            Traversal.inorder(root.left,l) 
            l.append(root.val )
            Traversal.inorder(root.right,l) 
        return l 
    @staticmethod
    def postorder(root,l): 
    
        if root is not None: 
            Traversal.postorder(root.left, l) 
            Traversal.postorder(root.right , l) 
            l.append(root.val )
        return l
    @staticmethod
    def preorder(root , l): 
    
        if root is not None: 

            l.append(root.val )
            Traversal.preorder(root.left , l) 
            Traversal.preorder(root.right , l) 
        return l
    @staticmethod
    def levelorder(root , l): 
        if root is None: 
            return
        q = deque([])
        q.append(root) 
        while len(q):
            current = q.popleft()
            l.append(current.val)  
            if current.left : 
                q.append(current.left) 
            if current.right : 
                q.append(current.right)
        return l

class TraversalWrapper :
    def inorder(self):
        '''
        return a list with the tree traversed with inorder
        '''

        return Traversal.inorder(self.root,[])
        
    
    def postorder(self):
        '''
        return a list with the tree traversed with postorder
        '''
        return Traversal.postorder(self.root , [])
        

    def preorder(self):
        '''
        return a list with the tree traversed with preorder
        '''
        return Traversal.preorder(self.root , [])
        


    def levelorder(self):
        '''
        return a list with the tree traversed with levelorder
        '''
        return Traversal.levelorder(self.root , [])
        

    def topologicalsort(self):
        '''
        return a list with the tree traversed with topologicalsort
        '''
        return Traversal.preorder(self.root , [])
        

    def bfs(self , val):
        '''
        searches for the value val using bfs on the tree
        '''
        if self.root is None: 
            return False
        q = deque([])
        q.append(self.root) 
        while len(q):
            current = q.popleft()
            if current.val == val :
                return True   
            if current.left : 
                q.append(current.left) 
            if current.right : 
                q.append(current.right)
        return False
    
    def dfs(self , val):
        '''
        searches for value val  using dfs on the tree
        '''
        stack = []
        stack.append(self.root)
        while len(stack):
            current = stack.pop()
            if current.val == val:
                return True
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return False
        

class Node :
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
    
    def __str__(self):
        return str(self.val)
