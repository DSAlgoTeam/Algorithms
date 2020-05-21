

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


class LinkedList:
    def __init__(self):
        """
        Creates a linked list.
        """
        self.head = None
        self.last = self.head
        self.length = 0

    def insert(self, value):
        """
        Inserts an element to the Linked List.

        params:
            value (Any): inserts the given value to the Linked List

        returns:
            None
        """
        node = Node(value)
        self.length += 1
        if not self.head:
            self.head = node
            self.last = self.head
            return
        self.last.next = node
        self.last = node

    def remove(self, value):
        """
        Removes an element from the Linked Lsit.

        params:
            value (Any): Value to be removed from 
        returns:
            None
        """
        if not self.head:
            raise Exception('Empty Linked List')
        node = self.head
        prev = node
        self.length -= 1
        if not self.head.next and self.head.value == value:
            self.head = None
            node = None
            return
        while node != None:
            if node.value == value:
                prev.next = prev.next.next
                del node
                return
            prev = node
            node = node.next
        raise ValueError('No such element in the Linked List')

    def isEmpty(self):
        """
        Checks if the FIFO structure is empty or not

        params:
            None
        returns
            (bool) : True if list is empty else False
        
        """
        return self.length == 0

    def size(self):
        """
        returns the size of the LIFO structure

        params:
            None
        returns:
            size(int): size of the LIFO structure.
        """
        return self.length


class FIFO(LinkedList):
    def __init__(self, value=None):
        """
        Starts the FIFO structure with given value

        params:
            value (Any): value of the first element of the FIFO structure
        """

        super(FIFO,self).__init__()
        if value:
            super(FIFO,self).insert(value)

        
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

class LIFO(LinkedList):
    def __init__(self, value=None):
        """
        Starts the LIFO structure with given value

        params:
            value (Any): value of the first element of the LIFO structure
        """
        super(LIFO,self).__init__()
        if value:
            super(LIFO,self).insert(value)

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
