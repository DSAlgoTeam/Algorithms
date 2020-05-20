from abc import ABCMeta , abstractmethod

class CommonFunctions(metaclass=ABCMeta) :
    ''' A common  Base Class for FIFO and LIFO data Structures implemented using lists '''        
    def __init__(self,value = None):
        """
        Initializes the LIFO/FIFO Structure with a value if provided .
        Args:
            value (Any): value of the first element .
        """
        self.items = []
        if value is not None :
            self.items.append(value)
    
    def is_empty(self) :
        """
        Returns True if FIFO/LIFO data structure is empty or else returns False
        Args:
            None
        Returns :
            bool : True if it is empty or else False
        """
        if(len(self.items)) == 0:
            return True
        else :
             return False

    

    
    @abstractmethod
    def insert(self,value) :
        pass
    @abstractmethod
    def remove(self,valur) :
        pass




class Stack(CommonFunctions) :
    def __init__(self,value = None):
        """
        Initializes the Stack with a value if provided .
        Args:
            value (Any): value of the first element .
        """
        super().__init__(value)
        

    def insert(self, item):
        """
        Inserts the item into the stack .
        Args:
            item(Any) : The object to be inserted into the stack
        
        returns:
            None
        """
        self.items.append(item)

    def remove(self) :
        """
        Returns the removed element from the stack .
        Args:
            None
        Raises :
        Exception
            If the stack Data Structure is empty
        returns:
            value (Any): value of element that is removed .
        """
        if len(self.items) == 0 :
            raise Exception('Stack Underflow')
            
        return self.items.pop()

    
    def peek(self) :
        """
        Returns the next Elemnt to be removed , but does not remove it .
        Args:
            None
        Raises :
        Exception
            If the stack Data Structure is empty
        returns:
            value (Any): value of element that will be removed next.
        """
        if self.is_empty() :
            raise Exception('Stack Underflow')
            
        return self.items[-1]

    def __str__(self) :
        '''Returns the LIFO data Structure as a Sring seprated by Spaces '''
        return " ".join(self.items)

    def __len__(self) :
        '''Returns the length LIFO data Structure  '''
        return len(self.items)

    

    


class Queue(CommonFunctions) :
    
    def __init__(self,value = None):
        """
        Initializes the Queue with a value if provided .
        Args:
            value (Any): value of the first element .
        """
        super().__init__(value)
        

    def insert(self,item ) :
        """
        Inserts the item into the Queue .
        Args:
            item(Any) : The object to be inserted into the Queue
        
        returns:
            None
        """
        self.items.append(item)

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
            raise Exception('queue undeflow')
            
        return self.items.pop(0)

    
    def peek(self) :
        """
        Returns the next Elemnt to be removed , but does not remove it .
        Args:
            None
        Raises :
        Exception
            If the queue Data Structure is empty
        returns:
            value (Any): value of element that will be removed next.
        """
        if self.is_empty() :
            raise Exception('queue undeflow')
            
        return self.items[0]

    def __str__(self) :
        '''Returns the LIFO data Structure as a Sring seprated by Spaces '''
        return " ".join(self.items)

    def __len__(self) :
        '''Returns the length LIFO data Structure  '''
        return len(self.items)



