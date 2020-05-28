from collections.abc import Iterable

class Heap:
    def __init__(self, iterable = None, min_heap = True):

        if not isinstance(iterable, (Iterable, type(None) )):
            raise ValueError('cannot make a heap of a non iterable value')
        
        if not isinstance(min_heap, bool):
            raise ValueError('min_heap should be either True or False only')

        self.heap = []
        self.min_heap = min_heap
        if iterable:
                for i in iterable:
                    self.insert(i)

    def insert(self, value):
        '''
        insert element into heap, maintaining the variant
        '''
        if value is None:
            raise ValueError('value to be inserted into heap can\'t be of type NoneType')
        if len(self.heap) == 0:
            self.heap.append(value)
            return
        self.heap.append(value)
        i = len(self.heap) - 1
        if self.min_heap:
            while i != 0 and (self.heap[self.parent(i)] > self.heap[i]):
                self.swap(i, self.parent(i))
                i = self.parent(i)
        else:
            while i != 0 and (self.heap[self.parent(i)] < self.heap[i]):
                self.swap(i, self.parent(i))
                i = self.parent(i)

    def peek(self):
        '''
        peek the topmost value in the Heap
        '''
        return self.heap[0]

    def remove(self):
        '''
        Removes the topmost element from the heap, maintaining the variant of heap
        '''
        if len(self.heap) < 1:
            return float('inf')
        if len(self.heap) == 1:
            return self.heap.pop()

        top = self.heap[0]
        self.heap[0] = self.heap.pop() # put last element in front
        self.heapify(0)
        return top
        
    def heapify(self, i):
        '''
        heapify method for heap, maintains the variant
        '''
        l = self.left(i)
        r = self.right(i)
        fn = min if self.min_heap else max
        smallest = i
        if l < len(self.heap):
            smallest = self.heap.index(fn(self.heap[l],self.heap[smallest]))
        if r < len(self.heap):
            smallest = self.heap.index(fn(self.heap[r],self.heap[smallest]))
        if smallest != i:
            self.swap(i,smallest)
            self.heapify(smallest)
        
    
    def left(self, idx):
        '''
        returns left child index of current index
        '''
        return 2*idx + 1

    def right(self,idx):
        '''
        returns right child index of current index
        '''
        return 2*idx + 2

    def parent(self,idx):
        '''
        returns parent index of current index
        '''
        return (idx-1) // 2
    
    def swap(self, idx1, idx2):
        '''
        swaps two values at given indexes in the heap
        '''
        self.heap[idx1],self.heap[idx2] = self.heap[idx2], self.heap[idx1]