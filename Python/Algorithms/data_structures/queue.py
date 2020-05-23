from linked_list import FIFO_LL
from lists import FIFO_List

class Queue(FIFO_LL):
    
    def first(self):
        return self.root

class Queue_List(FIFO_List):

    def first(self):
        return self.elements[0]