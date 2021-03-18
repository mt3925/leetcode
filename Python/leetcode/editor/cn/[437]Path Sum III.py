# You are given a binary tree in which each node contains an integer value. 
# 
#  Find the number of paths that sum to a given value. 
# 
#  The path does not need to start or end at the root or a leaf, but it must go 
# downwards
# (traveling only from parent nodes to child nodes). 
# 
#  The tree has no more than 1,000 nodes and the values are in the range -1,000,
# 000 to 1,000,000.
# 
#  Example:
#  
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
# 
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
# 
# Return 3. The paths that sum to 8 are:
# 
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
#  
#  Related Topics 树 
#  👍 765 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def pathSum(self, root: TreeNode, sum: int) -> int:
#         cnt = 0
#         def _find_path_cnt(node):
#             if not node:
#                 return
#             _find_path_cnt_head(node, 0)
#             _find_path_cnt(node.left)
#             _find_path_cnt(node.right)
#         def _find_path_cnt_head(node, total):
#             if not node:
#                 return
#             if node.val + total == sum:
#                 nonlocal cnt
#                 cnt += 1
#             _find_path_cnt_head(node.left, node.val + total)
#             _find_path_cnt_head(node.right, node.val + total)
#         _find_path_cnt(root)
#         return cnt

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        sum_map = collections.defaultdict(int)
        sum_map[0] = 1
        root_sum = 0
        rst = 0

        def _path_sum(node):
            if not node:
                return
            nonlocal root_sum, rst
            root_sum += node.val
            rst += sum_map[root_sum - sum]

            sum_map[root_sum] += 1

            _path_sum(node.left)
            _path_sum(node.right)

            sum_map[root_sum] -= 1
            root_sum -= node.val
        _path_sum(root)
        return rst

# leetcode submit region end(Prohibit modification and deletion)
