

class Node:
    def __init__(self, val, next = None):
        """
        Creates a linked list node with given value `val` and points to `next` node.

        params:
            val (Any): Value of the node
            next (Node): Next node in the linked list
        """
        self.value = val
        self.next = next


class FIFO:
    def __init__(self, value=None):
        """
        Starts the FIFO structure with given value

        params:
            value (Any): value of the first element of the FIFO structure
        """

        self.head = Node(value) if value else None
        self.last = head

    def insert(self, value):
        """
        Inserts an element to the FIFO structure.

        params:
            value (Any): inserts the given value to the FIFO structure

        returns:
            None
        """
        
        node = Node(value)
        self.last.next = node
        self.last = node

        if not self.head:
            self.head = node
        
    def remove(self):
        """
        Removes an element from given structure using FIFO fashion.

        params:
            None
        returns
            value (Any): returns the value of the removed element
        """
        if self.isEmpty():
            raise Exception("Empty FIFO structure")

        node = self.head

        if self.head == self.last:
            self.last = None
        self.head = self.head.next

        return node.value

    def peek(self):
        """
        Returns the value of the next element that will be removed from the structure. 
        But doesn't remove the element.

        params:
            None
        returns:
            value (Any): value of element that will be removed next.
        """
        if self.isEmpty():
            raise Exception("Empty FIFO structure")

        return self.head.value

    def isEmpty(self):
        """
        Checks if the FIFO structure is empty or not

        params:
            None
        returns
            (bool) : True if list is empty else False
        
        """
        return self.head == None

class LIFO:
    def _init__(self, value=None):
        """
        Starts the LIFO structure with given value

        params:
            value (Any): value of the first element of the LIFO structure
        """
        head = Node(value) if value else None
        self.head = head

    def insert(self,value):
        """
        Inserts an element to the LIFO structure.

        params:
            value (Any): inserts the given value to the FIFO structure

        returns:
            None
        """
        node = Node(value)
        node.next = self.head
        self.head = node

    def remove(self):
        """
        Removes an element from given structure using LIFO fashion.

        params:
            None
        returns
            value (Any): returns the value of the removed element
        """
        if self.isEmpty():
            raise Exception("EMPTY LIFO structure")
        node = self.head
        self.head = self.head.next
        return node.value

    def peek(self):
        """
        Returns the value of the next element that will be removed from the structure. 
        But doesn't remove the element.

        params:
            None
        returns:
            value (Any): value of element that will be removed next.
        """
        if self.isEmpty():
            raise Exception("EMPTY LIFO structure")
        return self.head.value

    def isEmpty(self):
        """
        Checks if the FIFO structure is empty or not

        params:
            None
        returns
            (bool) : True if list is empty else False
        
        """
        return self.head == None
             
