from abc import ABCMeta, abstractmethod
from stack_queue_array import Stack , Queue

from traversal import Node, TraversalWrapper


class BinaryTree(TraversalWrapper) :
    def __init__(self,value = None) :
        self.length = 0
        if value is not None :
            self.root = Node(value)   
            self.length +=1
            return 
        self.root = None
  
    def insert(self ,val = None) :
        '''
        inserts  a node  with the value provided
        '''
        if val is None :
            raise ValueError("NoneType Argument not Accepted")
        self.length +=1  
        q = Queue()
        q.insert(self.root)
   
        while (len(q)):  
            current_node = q.remove()
              
            if not current_node.left : 
                current_node.left = Node(val)  
                break
            elif not current_node.right: 
                current_node.right = Node(val)  
                break
            else:
                q.insert(current_node.left) 
                q.insert(current_node.right)
