# You are given an array of integers nums, there is a sliding window of size k w
# hich is moving from the very left of the array to the very right. You can only s
# ee the k numbers in the window. Each time the sliding window moves right by one 
# position. 
# 
#  Return the max sliding window. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1], k = 1
# Output: [1]
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [1,-1], k = 1
# Output: [1,-1]
#  
# 
#  Example 4: 
# 
#  
# Input: nums = [9,11], k = 2
# Output: [11]
#  
# 
#  Example 5: 
# 
#  
# Input: nums = [4,-2], k = 2
# Output: [4]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 105 
#  -104 <= nums[i] <= 104 
#  1 <= k <= nums.length 
#  
#  Related Topics 堆 Sliding Window 
#  👍 887 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         head = tail = ListNode(None, None)
#         head.nex = tail
#         tail.pre = head
#         rst = [0] * (len(nums) - k + 1)
#
#         def add(idx):
#             tmp = tail.pre
#             while tmp and tmp != head:
#                 if tmp.val > nums[idx]:
#                     break
#                 tmp.nex.pre = tmp.pre
#                 tmp.pre.nex = tmp.nex
#                 tmp = tmp.pre
#
#             node = ListNode(nums[idx], idx)
#             tail.pre.nex = node
#             node.pre = tail.pre
#             node.nex = tail
#             tail.pre = node
#
#         for idx in range(len(nums) - k + 1):
#             if idx == 0:
#                 for _idx in range(k):
#                     add(_idx)
#                 rst[idx] = head.nex.val
#             else:
#                 if head.nex.idx == idx - 1:
#                     head.nex.nex.pre = head
#                     head.nex = head.nex.nex
#                 add(idx + k - 1)
#                 rst[idx] = head.nex.val
#         return rst
#
#
# class ListNode:
#     def __init__(self, val, idx):
#         self.val = val
#         self.idx = idx
#         self.nex = None
#         self.pre = None

import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        rst = []
        for idx, item in enumerate(nums):
            while queue and nums[queue[-1]] <= item:
                queue.pop()
            queue.append(idx)
            if queue[0] == idx - k:
                queue.popleft()
            if idx >= k - 1:
                rst.append(nums[queue[0]])
        return rst

# leetcode submit region end(Prohibit modification and deletion)
