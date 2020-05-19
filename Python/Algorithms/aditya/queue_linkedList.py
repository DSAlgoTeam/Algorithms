import sys
class Node :
    def __init__(self,data) :
        self.data = data
        self.next = None

class Queue :
    def __init__(self) :
        self.head = None

    def isempty(self) :
        if self.head == None :
            return True
        return False

    def enqueue(self,data) :
        if self.isempty() :
            self.head = Node(data)
        else :
            itter = self.head
            while itter.next :
                itter = itter.next
            itter.next = Node(data)
    
    def dequeue(self) :
        if self.isempty() :
            sys.exit("Queue Underflow")
            
        temp = self.head
        self.head = self.head.next
        temp.next = None
        return temp.data
        
    def peek(self) :
        ''' gives the element about to be removed , but doesnt remove it'''
        if self.isempty() :
            sys.exit("Queue Underflow")
             
        return self.head.data

    def displayList(self) :

        node = self.head
        self.temp = []
        if self.isempty() :
            print('Empty Queue ')

        while(node != None) :
            self.temp.append(node.data)
            node = node.next
        
        return self.temp

    def length(self) :
        if self.isempty() :
            return 0
        else :
            count = 1
            node = self.head
            while node.next :
                node = node.next
                count += 1

            return count
    
# q = Queue()

# q.enqueue("adi")
# q.enqueue("ramu")
# q.enqueue("akash")
# q.enqueue("jayant")
# q.enqueue("arpit")

# print(q.dequeue())
# print(q.peek())
# print(q.displayList())
# print(q.length())
