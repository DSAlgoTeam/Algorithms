class Node(object):
    def __init__(self, val =None):
        self.val = val
        self.children = []

       


class N_Ary_Tree():

    def __init__(self, n_val):
        self.n_val = n_val
        self.root = None

    
    def levelOrderSort(self, node = None):
        '''
        function: sorting elements based on their level
        '''
        current = [node]
        while current:
            queue = []
            for i in current:
                print (i.val,end=" ")
                if i.children:
                    for k in i.children:
                        queue.append(k)
            print("\n")
            current = queue


    def dfs(self, node = None, key = None) -> bool:
        '''
        function: depth first search of an element in tree
        '''
        if not node: return False
        if node.val == key: return True
        return any([self.dfs(i, key) for i in node.children])


    def insert(self, node = None, val = None):
        '''
        function: insert element based on level order method
        '''

        if not self.root:
            self.root = Node(val)
            return

        queue = [node]

        while queue:
            current = queue.pop(0)

            if len(current.children) < self.n_val:
                current.children.append(Node(val))
                break
            for i in current.children:
                queue.append(i)

    def topoSort(self, node = Node, arr = []):
        '''
        function: sort elements based on pre_odrder method
        '''
        if not node:
            return
        arr.append(node.val)
        for i in node.children: self.topoSort(i,arr)

        return arr


    '''def delete(self, node = None, key = None):
        
        #function: delete the node with value = key
        

        if not self.root:
            print("Empty tree")

        if not node:
            return

        if not node.children:
            if node.val == key: 
                del node
            return

        if node.val == key:
            m = self.getLast()
            self.delete(self.root, m)
            node.val = m
            return
        for i in node.children: self.delete(i, key)
        '''


    def getLast(self, node = None):
        '''
        function: delete the last element and return the value
        '''
        current = [node]
        while current:
            queue = []
            for i in current:
                if i.children:
                    for k in i.children:
                        queue.append(k)
            if not queue: break
            current = queue
        value = current[-1].val
        return value