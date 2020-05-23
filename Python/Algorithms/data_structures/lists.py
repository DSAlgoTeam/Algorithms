from abc import ABCMeta, abstractmethod


class Abstract_List:
    
    @abstractmethod
    def insert(self,value):
        return
    
    @abstractmethod
    def remove(self,value):
        return

class List_Common(metaclass=ABCMeta):
    def __init__(self, value=None):
        self.elements = []
        if value is not None:
            self.elements.append(value)
        self.length = len(self.elements)

    def empty(self):
        return self.length == 0

    def __len__(self):
        return self.length

    def __str__(self):
        return "->".join(list(map(str, self.elements)))

class Common_List_Methods(object):

    @staticmethod
    def is_lifo_or_fifo(instance):
        if not isinstance(instance,(list, FIFO_List,LIFO_List)):
            raise Exception('Not a list instance')

    @staticmethod
    def is_empty(instance):
        Common_List_Methods.is_lifo_or_fifo(instance)
        if len(instance) == 0:
            raise Exception('Empty list instance')

    @staticmethod
    def push_back(instance,value):
        Common_List_Methods.is_lifo_or_fifo(instance)
        instance.elements.append(value)
        instance.length += 1
    
    @staticmethod
    def push_front(instance,value):
        Common_List_Methods.is_lifo_or_fifo(instance)
        instance.elements.insert(0,value)
        instance.length += 1
    
    @staticmethod
    def pop_back(instance):
        Common_List_Methods.is_lifo_or_fifo(instance)
        Common_List_Methods.is_empty(instance)
        instance.length -= 1
        return instance.elements.pop()

    @staticmethod
    def pop_front(instance):
        Common_List_Methods.is_lifo_or_fifo(instance)
        Common_List_Methods.is_empty(instance)
        instance.length -= 1
        return instance.elements.pop(0)



class FIFO_List(List_Common, Abstract_List):

    def insert(self,value):
        Common_List_Methods.push_back(self,value)

    def remove(self):
        return Common_List_Methods.pop_front(self)
    

class LIFO_List(List_Common,Abstract_List):
    
    def insert(self, value):
        Common_List_Methods.push_back(self,value)

    def remove(self):
        return Common_List_Methods.pop_back(self)