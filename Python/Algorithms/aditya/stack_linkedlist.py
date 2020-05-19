class Node :
    def __init__(self,data) :
        self.data = data
        self.next = None

class Stack :
    def __init__(self) :
        self.head = None

    def isempty(self) :
        if self.head == None :
            return True
        return False

    def push(self,data) :
        if self.isempty() :
            self.head = Node(data)
        else :
            temp = self.head
            self.head = Node(data)
            self.head.next = temp
    
    def pop(self) :
        if self.isempty() :
            print("Stack Underflow")
            return 
        temp = self.head
        self.head = self.head.next
        temp.next = None
        return temp.data
        
    def peek(self) :
        if self.isempty() :
            print("Stack Underflow")
            return 
        return self.head.data

    def displayList(self) :
        self.temp = []
        node = self.head
        if self.isempty() :
            print('Empty Stack')

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
            
