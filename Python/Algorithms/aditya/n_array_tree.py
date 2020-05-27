class Node :
    def __init__(self , val = None,) :
        if not val :
            raise Exception("Nonetype argument not accepted")

        self.val = val
        self.nextchild = []
        

    def insert(self,root , val , N) :
            
            if root.max_chidlen(N) :
                q = []
                count = 0
                q.append(root[count])
                while len(q) :
                    temp = q.pop(0)
                    if temp.max_chidlen(N) :
                        count +=1
                        q.append(root[count])
                    else :
                        temp.append(Node(val))
                        return

    def max_chidlen(self,N):
        return True if len(self.nextchild) == N else False

class nTree :
    N = 6
    def __init__(self,val):
        self.root  = Node(val)

    
          