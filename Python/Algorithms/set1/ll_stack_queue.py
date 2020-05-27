from abc import ABCMeta, abstractmethod

@abstractmethod
def push(self, val):
    return



class Node:
    def __init__(self, val):
        self.val = val
        self.next = None



class Basic(metaclass=ABCMeta):


    def __init__(self, val = None):
        
        self.head = None
        self.length = 0

        if val:
            self.head = Node(val)
            self.lenght +=1


    def push(self, val = None):
        if val:
            node = Node(val)
            if self.head:
                node.next = self.head
                self.head = node
            else: 
                self.head = node
            self.length +=1


    def isEmpty(self):
        return self.length == 0


    def top(self):
        if not self.isEmpty():
            return self.head.val
        raise IndexError("list index out of range")
    
    
    def __str__(self):

        string = "empty list"
        if self.head:
            string = "{}".format(self.head.val)
            node = self.head.next

            while node:
                string += "<--{}".format(node.val)
                node = node.next

        return string
        




class Stack(Basic):

    def __init__(self, val=None):
        super().__init__(val)



    def pop(self):
        if not self.isEmpty():
            node = self.head
            self.head = node.next
            self.length -=1
            node = None
            return
        raise Exception("Empty Stack")


    


class Queue(Basic):

    def __init__(self, val=None):
        super().__init__(val)

        self.end = None
        if val:
            self.head = self.end = Node(val)
            self.lenght +=1


    def pop(self):
        if self.isEmpty():
            raise Exception("Empty Queue")
        if self.head.next == None:
            self.head = None
        else:
            node = self.head
            while node.next:
                prev = node
                node = node.next
            prev.next = None
        self.length -= 1           