import sys
class Stack :
    def __init__(self):
        
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self) :
        if len(self.items) == 0 :
            sys.exit('Stack Underflow')
            
        return self.items.pop()

    def isempty(self) :
        if(len(self.items)) == 0:
            return True
        else :
             return False
    
    def peek(self) :
        if len(self.items) == 0 :
            sys.exit('Stack Underflow')
            
        return self.items[-1]

    def getStack(self) :
        return self.items

    def getsize(self) :
        return len(self.items)
# stack = Stack()
 
# stack.push('A')
# stack.push('D')
# stack.push('I')
# print(stack.pop())
# print(stack.getStack())
# print(stack.isempty())