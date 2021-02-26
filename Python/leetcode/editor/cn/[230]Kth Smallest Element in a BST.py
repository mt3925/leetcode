# Given the root of a binary search tree, and an integer k, return the kth (1-in
# dexed) smallest element in the tree. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
#  
# 
#  Example 2: 
# 
#  
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is n. 
#  1 <= k <= n <= 104 
#  0 <= Node.val <= 104 
#  
# 
#  
# Follow up: If the BST is modified often (i.e., we can do insert and delete ope
# rations) and you need to find the kth smallest frequently, how would you optimiz
# e? Related Topics 树 二分查找 
#  👍 354 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution1:
#     def kthSmallest(self, root: TreeNode, k: int) -> int:
#         self.tmp_rank = 1
#         self.rst = None
#         return self.find(root, k)
#
#     def find(self, root, k):
#         if not root:
#             return
#
#         self.find(root.left, k)
#         if self.tmp_rank == k:
#             self.rst = root.val
#             return
#         self.tmp_rank += 1
#         self.find(root.right, k)


# class Solution:
#     def kthSmallest(self, root: TreeNode, k: int) -> int:
#         items = self.find(root)
#         for _ in range(k - 1):
#             next(items, None)
#         return next(items, None)
#
#     def find(self, root):
#         if root:
#             yield from self.find(root.left)
#             yield root.val
#             yield from self.find(root.right)


# class Solution:
#     def kthSmallest(self, root, k):
#         from itertools import chain, islice
#         def gen(x): yield from chain(gen(x.left), [x.val], gen(x.right)) if x else ()
#         return next(islice(gen(root), k - 1, k))


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            min_node = stack.pop()
            k -= 1
            if k == 0:
                return min_node.val
            if min_node.right:
                root = min_node.right

# leetcode submit region end(Prohibit modification and deletion)
