'''
Stack that also gets min element at any point of time in O(1)
'''

class MinStackNode:
    def __init__(self, value = None, next = None):
        self.value = value
        self.minSoFar = float('inf')
        self.next = next

    def __add__(self, node):
        '''
        Magic method to add node to self
        '''
        if isinstance(node, MinStackNode):
            self.next = node
            return self
        else:
            raise TypeError("Inappropriate Add Node operation")
    
    def __str__(self):
        return str(self.value)

class MinStack:
    def __init__(self, node = None):
        self.head = None

    def insert(self, value):
        if value is None:
            raise ValueError('value cannot be of NoneType')
        node = value if isinstance(value, MinStackNode) else MinStackNode(value, self.head)
        node.next = self.head
        node.minSoFar = min(value, self.head.minSoFar if self.head else float('inf'))
        self.head = node
    
    def remove(self):
        if self.head is None:
            raise Exception('Empty stack, cannot remove element')
        node = self.head
        self.head = self.head.next
        return node.value
    
    def getMin(self):
        if self.head is None:
            raise Exception('Empty stack, cannot get minimum value')
        return self.head.minSoFar
    
    def top(self):
        if self.head is None:
            raise Exception('Empty stack, cannot get minimum value')
        return self.head.value
    
    def __str__(self):
        if self.head is None:
            return "Empty stack"
        node = self.head
        string = ''
        while node is not None:
            string += str(node) + ' '
            node = node.next
        return string

        