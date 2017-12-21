
class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def print_preorder(self):
        print self.value,
        if self.left:
            self.left.print_preorder()
        if self.right:
            self.right.print_preorder()

    def print_inorder(self):
        if self.left:
            self.left.print_inorder()
        print self.value,
        if self.right:
            self.right.print_inorder()

    def print_postorder(self):
        if self.left:
            self.left.print_postorder()
        if self.right:
            self.right.print_postorder()
        print self.value,


def construct(preorder, inorder):
    if not preorder or not inorder:
        return

    root_node = BinaryTreeNode(preorder[0])
    i = inorder.index(preorder[0])

    left_inorder = inorder[:i]
    right_inorder = inorder[i+1:]
    left_preorder = preorder[1:i+1]
    right_preorder = preorder[i+1:]

    root_node.left = construct(left_preorder, left_inorder)
    root_node.right = construct(right_preorder, right_inorder)
    return root_node


t = construct([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6])
t.print_preorder()
print ''
t.print_inorder()
print ''
t.print_postorder()
