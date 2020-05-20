
from abc import ABC ,abstractmethod 

class Node :
    def __init__(self,data) :
        """
        Creates a node with data and the next attribute is initialized to None.
        Args:
            data (Any): Value of the node
            
        """
        self.data = data
        self.next = None



class CommonLinkedList(ABC) :
    def __init__(self,value= None) :
        """
        Initializes the LInkedList with a node value if provided .
        Args:
            value (Any): value of the first element .
        """
        if value is not None :
            self.head = Node(value)
            self.length = 1
        else :
            self.head = None
            self.length = 0

    def is_empty(self) :
        """
        Returns True if FIFO/LIFO data structure is empty or else returns False
        Args:
            None
        Returns :
            bool : True if it is empty or else False
        """
        if self.head is None :
            return True
        return False
    
    def __len__(self) :
        '''Returns the length FIFO/LIFO data Structure  '''
        return self.length

    def __repr__(self) :
        '''Returns the FIFO/LIFO data Structure as a String '''
        node = self.head 
        string_rep = ""
        if self.is_empty(): 
            return "" 
          
        else: 
              
            while(node != None): 

                string_rep += " {} <-- ".format(node.data)  
                 
                node = node.next
            return string_rep
    

          
    

    @abstractmethod
    def insert(self,value) :
        pass
    @abstractmethod
    def remove(self,valur) :
        pass



class Stack(CommonLinkedList) :
    def __init__(self,value = None) :
        """
        Initializes the Stack with a node value if provided .
        Args:
            value (Any): value of the first node .
        """
        super().__init__(value)

    

    def insert(self,data) :
        """
        Inserts the item into the stack .
        Args:
            item(Any) : The object to be inserted into the stack
        
        returns:
            None
        """
        if self.is_empty() :
            self.head = Node(data)
        else :
            temp = self.head
            self.head = Node(data)
            self.head.next = temp
        self.length +=1
    
    def remove(self) :
        """
        Returns the removed node value from the stack .
        Args:
            None
        Raises :
        Exception
            If the stack Data Structure is empty
        returns:
            value (Any): node value of element that is removed .
        """
        if self.is_empty() :
            raise Exception("Stack Underflow")
            
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -=1
        return temp.data
        
    def peek(self) :
        """
        Returns the next node data to be removed , but does not remove it .
        Args:
            None
        Raises :
        Exception
            If the stack Data Structure is empty
        returns:
            value (Any): value of node that will be removed next.
        """
        if self.is_empty() :
            raise Exception("Stack Underflow")
            
        return self.head.data


    
    
        
            



class Queue(CommonLinkedList) :
    def __init__(self,value = None) :
        """
        Initializes the Queue with a node value if provided .
        Args:
            value (Any): value of the first element .
        """
        super().__init__(value)

    
    def insert(self,data) :
        """
        Inserts the data into the queue .
        Args:
            data(Any) : The object to be inserted into the data
        
        returns:
            None
        """
        if self.is_empty() :
            self.head = Node(data)
        else :
            itter = self.head
            while itter.next :
                itter = itter.next
            itter.next = Node(data)
        self.length +=1
    
    def remove(self) :
        """
        Returns the removed element from the stack .
        Args:
            None
        Raises :
        Exception
            If the queue Data Structure is empty
        returns:
            value (Any): value of element that is removed .
        """
        if self.is_empty() :
            raise Exception("Queue Underflow")
            
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -=1
        return temp.data
        
    def peek(self) :
        """
        Returns the next node data to be removed , but does not remove it .
        Args:
            None
        Raises :
        Exception
            If the queue Data Structure is empty
        returns:
            value (Any): value of node that will be removed next.
        """
        if self.is_empty() :
            raise Exception("Queue Underflow")
             
        return self.head.data

    
    

