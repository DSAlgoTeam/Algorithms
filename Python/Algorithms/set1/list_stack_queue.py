from abc import ABCMeta, abstractmethod

@abstractmethod
def remove(self, pos):
    return


class Basic(metaclass=ABCMeta):


    def __init__(self, val = None):

        self.list = []
        if val:
            self.list.append(val)
            

    def isEmpty(self):
        return False if self.list else True


    def __str__(self):
        if self.list:
            return ",".join(map(str,self.list))
        return "nothing to display"


    def insert(self, val = None):
        if val:
            self.list.append(val)

    
    def remove(self, pos = 0):

        if self.isEmpty():
            raise Exception("Empty List") 
                 
        temp = self.list[pos]
        del self.list[pos]
        return temp
        


    def top(self):
        if not self.isEmpty():
            return self.list[-1]
        raise IndexError("list index out of range") 
            







class Stack(Basic):

    def __init__(self, val=None):
        super().__init__(val)


    def remove(self):
        return super().remove(-1)




class Queue(Basic):

    def __init__(self, val=None):
        super().__init__(val)


    def remove(self):
        return super().remove(0)