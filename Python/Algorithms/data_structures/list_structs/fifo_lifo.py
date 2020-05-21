from abc import ABCMeta, abstractmethod


class Abstract_FIFO_LIFO:
    
    @abstractmethod
    def insert(self,value):
        return
    
    @abstractmethod
    def remove(self,value):
        return

class FIFO_LIFO_Common(metaclass=ABCMeta):
    def __init__(self, value=None):
        self.elements = []
        if value is not None:
            self.elements.append(value)
        self.length = len(self.elements)

    def empty(self):
        return Common_FIFO_LIFO_Methods.is_empty(self)

    def __len__(self):
        return self.length

    def __str__(self):
        return "->".join(list(map(str, self.elements)))

class Common_FIFO_LIFO_Methods(object):

    @staticmethod
    def is_lifo_or_fifo(instance):
        if not isinstance(instance,(FIFO_List,LIFO_List)):
            raise Exception('Not a FIFO or LIFO instance')

    @staticmethod
    def is_empty(instance):
        Common_FIFO_LIFO_Methods.is_lifo_or_fifo(instance)
        return len(instance) == 0

    @staticmethod
    def push_back(instance,value):
        Common_FIFO_LIFO_Methods.is_lifo_or_fifo(instance)
        instance.elements.append(value)
        instance.length += 1
    
    @staticmethod
    def push_front(instance,value):
        Common_FIFO_LIFO_Methods.is_lifo_or_fifo(instance)
        instance.elements.insert(0,value)
        instance.length += 1
    
    @staticmethod
    def pop_back(instance):
        Common_FIFO_LIFO_Methods.is_lifo_or_fifo(instance)
        if Common_FIFO_LIFO_Methods.is_empty(instance):
            raise Exception('Empty structure.')
        instance.length -= 1
        return instance.elements.pop()

    @staticmethod
    def pop_front(instance):
        Common_FIFO_LIFO_Methods.is_lifo_or_fifo(instance)
        if Common_FIFO_LIFO_Methods.is_empty(instance):
            raise Exception('Empty structure.')
        instance.length -= 1
        return instance.elements.pop(0)



class FIFO_List(FIFO_LIFO_Common):

    def insert(self,value):
        Common_FIFO_LIFO_Methods.push_back(self,value)

    def remove(self):
        return Common_FIFO_LIFO_Methods.pop_front(self)
    

class LIFO_List(FIFO_LIFO_Common):
    
    def insert(self, value):
        Common_FIFO_LIFO_Methods.push_back(self,value)

    def remove(self):
        return Common_FIFO_LIFO_Methods.pop_back(self)