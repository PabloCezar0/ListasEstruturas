from arvore import BinaryTree, Node



tree = BinaryTree(7)
tree.root.left = Node(18)
tree.root.right = Node(14)
tree.root.left.left = Node(18)
tree.root.right.left = Node(18)
tree.root.left.left.right = Node(18)


print(tree.height())
