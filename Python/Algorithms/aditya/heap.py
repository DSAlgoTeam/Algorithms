
class Heap :
    HEAP_SIZE = 10

    def __init__(self,N,type = 'min') :
        Heap.HEAP_SIZE = N
        self._heap = [None]*Heap.HEAP_SIZE
        self.count = 0
        self.type = type

    def __len__(self) :
        return self.count
    

    def right(self,i) :
        return 2*i + 2
    
    def left(self,i):
        return 2*i + 1
    
    def parent(self, i) :
        return (i-1)//2

    def capacity( self ):
        return self.HEAP_SIZE

    def insert(self,value) :
        if self.count >= self.capacity() :
             Exception("Cannot add to full heap")
        self._heap[self.count] = value
        self.count +=1
        if self.type == 'min' :
            self._siftUp(self.count - 1)
        else :
            self._siftUpMax(self.count - 1)

    def extract(self) :
        if self.count == 0 :
            raise Exception("Cannot Extract from empty Heap")
        value  = self._heap[0]
        self.count -=1
        self._heap[0] = self._heap[self.count]
        if self.type == 'min':
            self._siftDown(0)
        else :
            self._siftDownMax(0)
        return value

    def _siftUpMax( self, ndx ):
        if ndx > 0 :
            parent = self.parent(ndx)
            if self._heap[ndx] > self._heap[parent] : 
                tmp = self._heap[ndx]
                self._heap[ndx] = self._heap[parent]
                self._heap[parent] = tmp
                self._siftUpMax( parent )
    
    def _siftUp( self, ndx ):
        if ndx > 0 :
            parent = self.parent(ndx)
            if self._heap[ndx] < self._heap[parent] : 
                tmp = self._heap[ndx]
                self._heap[ndx] = self._heap[parent]
                self._heap[parent] = tmp
                self._siftUp( parent )
    
    def _siftDown(self,ndx) :
        l = self.left(ndx)
        r = self.right(ndx)
        smallest  = ndx
        if l < self.count and self._heap[l] <= self._heap[ndx] :
            smallest = l
        elif r < self.count and self._heap[r] <= self._heap[smallest] :
            smallest = r
        
        if smallest != ndx :
            self._heap[ndx] , self._heap[smallest] =   self._heap[smallest] , self._heap[ndx] 
            self._siftDown(smallest)

    def _siftDownMax(self,ndx) :
        l = self.left(ndx)
        r = self.right(ndx)
        largest  = ndx
        if l < self.count and self._heap[l] >= self._heap[ndx] :
            largest = l
        elif r < self.count and self._heap[r] >= self._heap[largest] :
            largest = r
        
        if largest != ndx :
            self._heap[ndx] , self._heap[largest] =   self._heap[largest] , self._heap[ndx] 
            self. _siftDownMax(largest)
    
