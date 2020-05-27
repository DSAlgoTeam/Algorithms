from Bin_tree_bst import Binary_tree
from Bin_tree_bst import Binary_search_tree



btree = Binary_search_tree(6)

btree.insert(10)
btree.insert(2)
btree.insert(3)
btree.insert(4)
btree.insert(5)


btree.preOrder(btree.root)
btree.inOrder(btree.root)
print(btree.topoSort(btree.root))
btree.levelOrderTraversal(btree.root)
print(btree.dfs(btree.root, 10))