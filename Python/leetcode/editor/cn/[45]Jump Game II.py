# Given an array of non-negative integers nums, you are initially positioned at 
# the first index of the array. 
# 
#  Each element in the array represents your maximum jump length at that positio
# n. 
# 
#  Your goal is to reach the last index in the minimum number of jumps. 
# 
#  You can assume that you can always reach the last index. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 
# step from index 0 to 1, then 3 steps to the last index.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,3,0,1,4]
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 1000 
#  0 <= nums[i] <= 105 
#  
#  Related Topics 贪心算法 数组 
#  👍 911 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         dp = [106] * len(nums)
#         dp[0] = 0
#         last = 0
#         for i in range(0, len(nums)):
#             last = max(last - 1, nums[i])
#             for j in range(i + 1, min(i + last + 1, len(nums))):
#                 dp[j] = min(dp[j], dp[i] + 1)
#         return dp[-1]


class Solution:
    def jump(self, nums: List[int]) -> int:
        step_last_e = 0  # 当前步数区间终点
        step_e = 0  # 当前步数能到达的最远位置
        step_cnt = 0  # 下一步数区间的步数
        for i in range(0, len(nums) - 1):
            step_e = max(i + nums[i], step_e)
            if i == step_last_e:
                step_cnt += 1
                step_last_e = step_e
        return step_cnt

# leetcode submit region end(Prohibit modification and deletion)
