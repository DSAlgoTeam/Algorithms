from fifo_lifo import FIFO_List

class Queue(FIFO_List):
    def first(self):
        return self.elements[0]