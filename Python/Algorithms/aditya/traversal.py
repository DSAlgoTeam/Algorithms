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
    
    @staticmethod
    def preorder(root , l): 
    
        if root is not None: 

            l.append(root.val )
            Traversal.preorder(root.left , l) 
            Traversal.preorder(root.right , l) 

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
        return Traversal.inorder(self.root,[])
        
    
    def postorder(self):
        return Traversal.postorder(self.root , [])
        

    def preorder(self):
        return Traversal.preorder(self.root , [])
        


    def levelorder(self):
        return Traversal.levelorder(self.root , [])
        

    def topologicalsort(self):
        return Traversal.preorder(self.root , [])
        

    def bfs(self , v):
        return True if v in Traversal.levelorder(self.root , []) else False
    def dfs(self , v):
        return True if v in Traversal.inorder(self.root , []) else False
        

class Node :
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
    
    def __str__(self):
        return str(self.val)
