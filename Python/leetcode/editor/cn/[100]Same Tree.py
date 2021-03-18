# Given the roots of two binary trees p and q, write a function to check if they
#  are the same or not. 
# 
#  Two binary trees are considered the same if they are structurally identical, 
# and the nodes have the same value. 
# 
#  
#  Example 1: 
# 
#  
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: p = [1,2], q = [1,null,2]
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in both trees is in the range [0, 100]. 
#  -104 <= Node.val <= 104 
#  
#  Related Topics 树 深度优先搜索 
#  👍 573 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return next(self._is_same(p, q), True)

    def _is_same(self, p, q):
        if p == q:
            return
        if not p or not q:
            yield False
        if p.val != q.val:
            yield False
        yield from self._is_same(p.left, q.left)
        yield from self._is_same(p.right, q.right)

# leetcode submit region end(Prohibit modification and deletion)
