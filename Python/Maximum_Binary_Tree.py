# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        """Time complexity : O(n^2).  一般情况下 O(nlogn)
        Space complexity : O(n)
        """
        if not nums:
            return None

        max_idx = 0
        max = nums[0]
        for idx, i in enumerate(nums):
            if i > max:
                max = i
                max_idx = idx

        root = TreeNode(max)
        root.left = self.constructMaximumBinaryTree(nums[0:max_idx])
        root.right = self.constructMaximumBinaryTree(nums[max_idx + 1:])
        return root

    def constructMaximumBinaryTree2(self, nums: List[int]) -> TreeNode:
        """Time complexity : O(n)"""
        stack = []

        for x in nums:
            n = TreeNode(x)
            while stack and x > stack[-1].val:
                n.left = stack.pop()

            if stack:
                stack[-1].right = n
            stack.append(n)

        return stack[0]
