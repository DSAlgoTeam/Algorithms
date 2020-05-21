from fifo_lifo import LIFO_List

class Stack(LIFO_List):
    def top(self):
        return self.elements[-1]