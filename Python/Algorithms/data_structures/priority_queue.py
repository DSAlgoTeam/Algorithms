from heap import Heap

class PriorityQueue(Heap):
    def __init__(self, iterable=None, max_queue = True):
        super(PriorityQueue, self).__init__(iterable,max_queue)
        self.__queue = self.heap