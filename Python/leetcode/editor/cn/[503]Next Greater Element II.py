# 
# Given a circular array (the next element of the last element is the first elem
# ent of the array), print the Next Greater Number for every element. The Next Gre
# ater Number of a number x is the first greater number to its traversing-order ne
# xt in the array, which means you could search circularly to find its next greate
# r number. If it doesn't exist, output -1 for this number.
#  
# 
#  Example 1: 
#  
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; The number 2 can't find n
# ext greater number; The second 1's next greater number needs to search circularl
# y, which is also 2.
#  
#  
# 
#  Note:
# The length of given array won't exceed 10000.
#  Related Topics 栈 
#  👍 401 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        rst = [-1] * len_nums
        stack = []
        for ori_idx in range(len_nums * 2):
            idx = ori_idx % len_nums
            item = nums[idx]
            while stack and item > nums[stack[-1]]:
                cur = stack.pop()
                rst[cur] = item
            if ori_idx < len_nums:
                stack.append(idx)
        return rst

# leetcode submit region end(Prohibit modification and deletion)
