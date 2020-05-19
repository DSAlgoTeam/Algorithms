import sys
class Queue :
    
    def __init__(self):
        
        self.items = []

    def enqueue(self,item ) :
        self.items.append(item)

    def dequeue(self) :
        if self.isempty() :
            sys.exit('queue undeflow')
            
        return self.items.pop(0)

    def isempty(self) :
        if len(self.items) == 0 :
            return True
        return False
    def peek(self) :
        if self.isempty() :
            sys.exit('queue undeflow')
            
        return self.items[0]

    def getsize(self) :
        return len(self.items)

    def getQueue(self) :
        return self.items

    
# q = Queue()

# q.enqueue('a')
# q.enqueue('b')
# q.enqueue('c')
# print(q.getsize())
# print(q.isempty())
# print(q.getsize())
# print(q.getQueue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())