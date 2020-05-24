from abc import ABCMeta, abstractmethod
from collections import deque

from traversal import Node, TraversalWrapper


class BinaryTree(TraversalWrapper) :
    def __init__(self,value = None) :
        
        if value is not None :
            self.root = Node(value)    
        self.root = None
  
    def insert(self ,val = None) :
        if val is None :
            raise ValueError("NoneType Argument not Accepted")
          
        q = deque([])
        q.append(self.root)
   
        while (len(q)):  
            current_node = q.popleft()
              
            if not current_node.left : 
                current_node.left = Node(val)  
                break
            elif not current_node.right: 
                current_node.right = Node(val)  
                break
            else:
                q.append(current_node.left) 
                q.append(current_node.right)
