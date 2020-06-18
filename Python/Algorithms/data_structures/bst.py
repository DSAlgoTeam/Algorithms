from Python.Algorithms.data_structures.binary_tree import CommonTreeMethods, Abstract_Tree


class BST(CommonTreeMethods,Abstract_Tree):
    '''
    Constructs a binary search tree.

    '''
    def insert(self,value):
        if self.create_root_if_none(value):
            return
        self.numOfNodes += 1
        temp = self.root
        while temp is not None:
            if value < temp.value:
                if temp.left:
                    temp = temp.left
                    continue
                else:
                    temp.left = self.make_node(value)
                    break
            else :
                if temp.right:
                    temp = temp.right
                    continue
                else:
                    temp.right = self.make_node(value)
                    break
    
        