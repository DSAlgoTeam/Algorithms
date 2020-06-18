from Python.Algorithms.data_structures.linked_list import FIFO_LL
from Python.Algorithms.data_structures.lists import FIFO_List

class Queue(FIFO_LL):
    
    def first(self):
        return self.root

class Queue_List(FIFO_List):

    def first(self):
        return self.elements[0]