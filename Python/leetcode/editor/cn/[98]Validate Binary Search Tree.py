# Given the root of a binary tree, determine if it is a valid binary search tree
#  (BST). 
# 
#  A valid BST is defined as follows: 
# 
#  
#  The left subtree of a node contains only nodes with keys less than the node's
#  key. 
#  The right subtree of a node contains only nodes with keys greater than the no
# de's key. 
#  Both the left and right subtrees must also be binary search trees. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: root = [2,1,3]
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 104]. 
#  -231 <= Node.val <= 231 - 1 
#  
#  Related Topics 树 深度优先搜索 递归 
#  👍 943 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        val = None

        def valid(root):
            if not root:
                return

            yield from valid(root.left)
            nonlocal val
            if val is not None:
                if root.val <= val:
                    yield False
            val = root.val
            yield from valid(root.right)
        return next(valid(root), None) is None


# leetcode submit region end(Prohibit modification and deletion)
