from traversal import TraversalWrapper , Node



class BinarySearchTreeFunctions :
    @staticmethod
    def insert( root, val): 
        '''
        inserts  a node recursively with the value provided
        '''
        if root is None: 
            return Node(val) 
    
        if val < root.val: 
            root.left = BinarySearchTreeFunctions.insert(root.left, val) 
        else: 
            root.right = BinarySearchTreeFunctions.insert(root.right, val) 
        return root 

    


class BinarySearchTree(TraversalWrapper) :

    def __init__(self,key=None) :
        if key is not None :
            self.root = Node(key)
            self.length = 1
        else :
            self.root = None
            self.length = 0 

    def insert(self,val): 
        '''
        inserts  a node recursively with the value provided
        '''
        self.root =  BinarySearchTreeFunctions.insert(self.root,val)
        self.length +=1
    # def delete(self,val) :

        
    #     self.root = BinarySearchTreeFunctions.delete(self.root,val)



