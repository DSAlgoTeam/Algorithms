from Python.Algorithms.data_structures.linked_list import LIFO_LL
from Python.Algorithms.data_structures.lists import LIFO_List

class Stack(LIFO_LL):
    
    def top(self):
        return self.root

class Stack_List(LIFO_List):

    def top(self):
        return self.elements[-1]