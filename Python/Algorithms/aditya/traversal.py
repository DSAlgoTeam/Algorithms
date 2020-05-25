from stack_queue_array import Stack , Queue
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
    def levelorder(root ,val, l): 
        if root is None: 
            return False
        q = Queue()
        q.insert(root) 
        while len(q):
            current = q.remove()
            l.append(current.val)
            if current.val == val :
                return (True,l)   
            if current.left : 
                q.insert(current.left) 
            if current.right : 
                q.insert(current.right)
        return (False,l)

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
        


    def levelorder(self, val):
        '''
        searches for the value val using bfs on the tree and returns the traversal and bool indicating 
        weather item was found or not . 
        '''
        return Traversal.levelorder(self.root ,val , [])
        

    def topologicalsort(self):
        '''
        return a list with the tree traversed with topologicalsort
        '''
        return Traversal.preorder(self.root , [])
        

    def bfs(self , val):
        '''
        searches for the value val using bfs on the tree and returns the traversal and bool indicating 
        weather item was found or not . 
        '''

        if self.root is None: 
            return False
        q = Queue()
        l= []
        q.insert(self.root) 
        while len(q):
            current = q.remove()
            l.append(current.val)
            if current.val == val :
                return (True,l)   
            if current.left : 
                q.insert(current.left) 
            if current.right : 
                q.insert(current.right)
        return (False,l)
    
    def dfs(self , val):
        '''
        searches for value val  using dfs on the tree
        '''
        stack = Stack()
        stack.insert(self.root)
        while len(stack):
            current = stack.remove()
            if current.val == val:
                return True
            if current.right:
                stack.insert(current.right)
            if current.left:
                stack.insert(current.left)
        return False
        

class Node :
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
    
    def __str__(self):
        return str(self.val)


