from binary_tree import CommonTreeMethods, Abstract_Tree

from stack import Stack

class BST(CommonTreeMethods,Abstract_Tree):
    '''
    Constructs a binary search tree.

    '''
    def insert(self,value):
        if self.create_root_if_none(value):
            return
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
    
    def inorder(self, node = None, fn = print):
        '''
        returns an iterable containing all the elements after inorder traversal

        '''
        if node is None:
            node = self.root
        if node.left:
            self.inorder(node.left,fn)

        fn(node.value)
        
        if node.right:
            self.inorder(node.right,fn)

    def preorder(self, node = None, fn = print):
        '''
        returns an iterable containing all the elements after preorder traversal

        '''
        if node is None:
            node = self.root
        
        fn(node.value)
        if node.left:
            self.inorder(node.left,fn)
        if node.right:
            self.inorder(node.right,fn)
    
    def postorder(self, node = None, fn = print):
        '''
        returns an iterable containing all the elements after preorder traversal

        '''
        if node is None:
            node = self.root
        
        if node.left:
            self.inorder(node.left,fn)

        if node.right:
            self.inorder(node.right,fn)

        fn(node.value)
    
    # TODO: DFS, BFS and Topological sorting.

    # def dfs(self,fn = print):
        