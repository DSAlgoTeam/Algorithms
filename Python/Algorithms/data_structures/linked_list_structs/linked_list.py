from abc import ABCMeta, abstractmethod

class AbstractLL(metaclass = ABCMeta):
    '''
    Abstraction of LinkedList Class
    '''
    @abstractmethod
    def insert(self, value):
        return

    @abstractmethod
    def remove(self):
        return

class CommonSingleLLMethods(object):
    '''
    Generic SinglyLinkedList utility
    '''
    def __init__(self, value = None):
        '''
        Constructor to initializa the LL requires a value.
        '''
        self.root = None
        self.length = 0
        if value is not None:
            self.root = self.make_node(value)
            self.length = 1

    def create_root_if_none(self, value):

        if self.root is None:
            self.root = self.make_node(value)
            return True

        return False

    def make_node(self, value):
        if value is None:
            raise ValueError("Nonetype Arguement Not expected")
        return value if isinstance(value, Node) else Node(value)

    def check_remove_root(self):
        '''
        Helper function to check and remove if it has no nodes or 1 node.
        '''   
        if self.root is None:
            return True
        if self.root.next is None:
            self.root = None
            self.length -= 1
            return True
        
        return False

    def empty(self):
        return self.root is None

    def __len__(self):
        return self.length

    def __str__(self):
        temp_node = self.root
        string_ll = self.root.value if self.root is not None else ""
        while temp_node.next is not None:
            temp_node = temp_node.next
            string_ll = "{0}->{1}".format(string_ll, str(temp_node))

        return string_ll

class SingleLinkedListCommon(object):

    @staticmethod
    def is_ll_instance(instance):
        if not isinstance(instance, (LinkedList, FIFO_LL, LIFO_LL)):
            raise Exception("Not a LL Instance")


    @staticmethod
    def push_back(instance, value):
        '''
        Pushes at the tail of the Linked List
        '''
        SingleLinkedListCommon.is_ll_instance(instance) 

        if instance.create_root_if_none(value):
            instance.length = 1
            return

        temp_node = instance.root

        while temp_node.next is not None:
            temp_node = temp_node.next

        temp_node += instance.make_node(value)
        # temp_node.next = instance.make_node(value)
        instance.length += 1

    @staticmethod
    def push_front(instance, value):
        '''
        Pushes at the head of the LinkedList
        '''
        SingleLinkedListCommon.is_ll_instance(instance) 

        if instance.create_root_if_none(value):
            instance.length = 1
            return

        value = instance.make_node(value)
        value += instance.root
        instance.root = value
        instance.length += 1

    @staticmethod
    def pop_back(instance):
        '''
        remove from the end of the linked list
        '''
        SingleLinkedListCommon.is_ll_instance(instance) 

        if instance.check_remove_root():
            return
        
        temp_node = instance.root
        while temp_node.next.next is not None:
            temp_node = temp_node.next
        
        temp_node.next = None
        instance.root = temp_node
        instance.length -= 1 

    @staticmethod
    def pop_front(instance):
        '''
        remove from the head of the LinkedList
        '''
        SingleLinkedListCommon.is_ll_instance(instance) 
        
        if instance.check_remove_root():
            return

        instance.root = instance.root.next
        instance.length -= 1

class FIFO_LL(AbstractLL, CommonSingleLLMethods):
    '''
    FIFO Linked List Data Structure
    '''
    def insert(self, value):
        SingleLinkedListCommon.push_back(self, value)
    
    def remove(self):
        if self.empty():
            raise Exception('Empty FIFO strcture')
        value = self.root.value
        SingleLinkedListCommon.pop_front(self)
        return value

class LIFO_LL(AbstractLL, CommonSingleLLMethods):
    '''
    LIFO Linked List Data Structure
    '''
    def insert(self, value):
        SingleLinkedListCommon.push_front(self, value)

    def remove(self):
        if self.empty():
            raise Exception('Empty LIFO strcture')
        value = self.root.value
        SingleLinkedListCommon.pop_front(self)
        return value

class LinkedList(CommonSingleLLMethods):

    '''
    Generic Linked List with more features
    '''

    def push_back(self, value):
        SingleLinkedListCommon.push_back(self, value)

    def push_front(self, value):
        SingleLinkedListCommon.push_back(self, value)

    def pop_back(self):
        SingleLinkedListCommon.pop_back(self)

    def pop_front(self):
        SingleLinkedListCommon.pop_front(self)

class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None

    def __add__(self, node):
        '''
        Add macgic method to add node to self
        '''
        if isinstance(node, Node):
            self.next = node
            return self
        else:
            raise TypeError("Inappropriate Add Node operation")
    
    def __str__(self):
        return str(self.value)