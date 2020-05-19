
class FIFO:
    def __init__(self, value = None):
        """
        Starts the FIFO structure with given value

        params:
            value (Any): value of the first element of the FIFO structure
        """
        self.array = []
        if value:
            self.array.append(value)
        self.length = len(self.array)

    def insert(self,value):
        """
        Inserts an element to the FIFO structure.

        params:
            value (Any): inserts the given value to the FIFO structure

        returns:
            None
        """
        self.array.append(value)
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
            raise Exception("Can't remove element from empty structure")
        
        value = self.array[0]
        del self.array[0]
        self.length -= 1

        return value
    
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

        return self.array[0]
    
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
        returns the size of the FIFO structure

        params:
            None
        returns:
            size(int): size of the FIFO structure.
        """
        return self.length

class LIFO:
    def __init__(self, value = None):
        """
        Starts the LIFO structure with given value

        params:
            value (Any): value of the first element of the LIFO structure
        """
        self.array = []
        if value:
            self.array.append(value)
        self.length = len(self.array)

    def insert(self, value):
        """
        Inserts an element to the LIFO structure.

        params:
            value (Any): inserts the given value to the FIFO structure

        returns:
            None
        """

        self.array.append(value)
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

        value = self.array[-1]
        del self.array[-1]
        self.length -= 1

        return value

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
            raise Exception("Can't peek in an empty LIFO structure")
        return self.array[-1]

    def isEmpty(self):
        """
        Checks if the LIFO structure is empty or not

        params:
            None
        returns
            (bool) : True if FIFO structure is empty else False
        
        """
        return self.length == 0

    def size(self):
        """
        returns the size of the LIFO structure

        params:
            None
        returns:
            size(int): size of the FIFO structure.
        """
        return self.length