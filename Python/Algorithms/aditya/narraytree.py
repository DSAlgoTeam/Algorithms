class TreeNode :
    def __init__(self, val) :
        self.val = val
        self.firstchild = None
        self.nextsibling = None

    def get_num_children(self ) :
        count = 1
        if  self.firstchild is None :
            return 0
        else :
            curr = self.firstchild
            while curr.nextsibling :
                count +=1
                curr = curr.nextsibling
            return count

class NArrayTree :
    
    def __init__(self,N) :
        self.N = N
        self.root = None

    def insert(self, val) :
        if self.root is None :
            self.root = TreeNode(val)
            return 
        q = []
        q.append(self.root)
        while len(q) :
            temp = q.pop(0)
            if temp.get_num_children() < self.N :
                if temp.firstchild is None :
                    temp.firstchild = TreeNode(val)
                    return
                else :
                    temp = temp.firstchild    
                    while temp.nextsibling is not None:
                        temp = temp.nextsibling
                    temp.nextsibling = TreeNode(val)
                    return
            else :
                temp = temp.firstchild
                q.append(temp)
                while temp.nextsibling is not None:
                    temp = temp.nextsibling
                    q.append(temp)
            
    def levelorder(self) :
        if self.root is None :
            print("")
        q = []
        q.append(self.root)
        while len(q) :
            temp = q.pop(0)
            print(temp.val)
            if  temp.firstchild is not None :
                child = temp.firstchild
                q.append(child)
                while(child.nextsibling):
                    child = child.nextsibling
                    q.append(child)
    
    def bfs(self,key) :
        if self.root is None :
            print("")
        q = []
        q.append(self.root)
        while len(q) :
            temp = q.pop(0)
            print(temp.val)
            if temp.val == key :
                return True
            if  temp.firstchild is not None :
                child = temp.firstchild
                q.append(child)
                while(child.nextsibling):
                    child = child.nextsibling
                    q.append(child)
        return False    
    
    def dfs(self) :
        #not working properly
        if self.root is None :
            print("")
        stack = []
        stack.append(self.root)
        while len(stack) :
            temp = stack.pop()
            print(temp.val)
            if  temp.firstchild is not None :
                child = temp.firstchild
                stack.append(child)
                while(child.nextsibling):
                    child = child.nextsibling
                    stack.append(child)



        
    


