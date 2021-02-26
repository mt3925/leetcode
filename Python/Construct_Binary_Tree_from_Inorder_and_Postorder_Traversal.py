# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder[-1])
        left_node_cnt = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:left_node_cnt], postorder[:left_node_cnt])
        root.right = self.buildTree(inorder[left_node_cnt + 1:], postorder[left_node_cnt: -1])
        return root
