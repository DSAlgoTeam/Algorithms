

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
        self.last = self.head
        self.length = 1 if self.head else 0

    def insert(self, value):
        """
        Inserts an element to the FIFO structure.

        params:
            value (Any): inserts the given value to the FIFO structure

        returns:
            None
        """
        
        node = Node(value)
        if not self.head:
            self.head = node
            self.last = self.head
        self.last.next = node
        self.last = node
        self.length += 1
        
    def remove(self):
        """
        Removes an element from given structure using FIFO fashion.

        params:
            None
        returns
            value (Any): returns the value of the removed element
        """
        if self.isEmpty():
            raise Exception("Can't remove element from empty FIFO structure")

        node = self.head

        if self.head == self.last:
            self.last = None
        self.head = self.head.next
        self.length -= 1

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
            raise Exception("Can't peek in empty FIFO structure")

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

    def size(self):
        """
        returns the size of the FIFO structure

        params:
            None
        returns:
            size(int): size of the FIFO structure.
        """
        return self.length

class LIFO:
    def __init__(self, value=None):
        """
        Starts the LIFO structure with given value

        params:
            value (Any): value of the first element of the LIFO structure
        """
        head = Node(value) if value else None
        self.head = head
        self.length = 1 if self.head else 0

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
        self.length += 1

    def remove(self):
        """
        Removes an element from given structure using LIFO fashion.

        params:
            None
        returns
            value (Any): returns the value of the removed element
        """
        if self.isEmpty():
            raise Exception("Can't remove element from an empty LIFO structure")
        node = self.head
        self.head = self.head.next
        self.length -= 1
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
    
    def size(self):
        """
        returns the size of the LIFO structure

        params:
            None
        returns:
            size(int): size of the LIFO structure.
        """
        return self.length
