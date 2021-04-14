# You are given a list of non-negative integers, a1, a2, ..., an, and a target, 
# S. Now you have 2 symbols + and -. For each integer, you should choose one from 
# + and - as its new symbol. 
# 
#  Find out how many ways to assign symbols to make sum of integers equal to tar
# get S. 
# 
#  Example 1: 
# 
#  
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 
# 
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 
# There are 5 ways to assign symbols to make the sum of nums be target 3.
#  
# 
#  
#  Constraints: 
# 
#  
#  The length of the given array is positive and will not exceed 20. 
#  The sum of elements in the given array will not exceed 1000. 
#  Your output answer is guaranteed to be fitted in a 32-bit integer. 
#  
#  Related Topics 深度优先搜索 动态规划 
#  👍 614 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         num_cnt = len(nums)
#         table = {}
#
#         def dp(idx, total):
#             if (idx, total) in table:
#                 return table[(idx, total)]
#             if idx >= num_cnt:
#                 if total == 0:
#                     return 1
#                 return 0
#             cnt = dp(idx + 1, total - nums[idx])
#             cnt += dp(idx + 1, total + nums[idx])
#             table[(idx, total)] = cnt
#             return cnt
#         return dp(0, S)


# class Solution:
#     def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         sum_nums = sum(nums)
#         if sum_nums < S or (sum_nums + S) % 2 == 1:
#             return 0
#
#         need_sum = (sum_nums + S) // 2
#         dp_pre = [-1 for _ in range(need_sum + 1)]
#         dp = [-1 for _ in range(need_sum + 1)]
#         for idx in range(0, len(nums) + 1):
#             for total in range(0, need_sum + 1):
#                 if idx == 0:
#                     if total == 0:
#                         dp[total] = 1
#                     else:
#                         dp[total] = 0
#                 else:
#                     if total == 0:
#                         dp, dp_pre = dp_pre, dp
#                     if total - nums[idx - 1] >= 0:
#                         dp[total] = dp_pre[total] + dp_pre[total - nums[idx - 1]]
#                     else:
#                         dp[total] = dp_pre[total]
#         return dp[need_sum]


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        sum_nums = sum(nums)
        if sum_nums < S or (sum_nums + S) % 2 == 1:
            return 0

        # A代表加的集合  B代表减的集合
        # sum(A) + sum(B) = sum(nums)
        # sum(A) - sum(B) = S    sum(B) = sum(A) - S
        # sum(A) + (sum(A) - S) = sum(nums)
        # sum(A) = (sum(nums) + S) / 2
        need_sum = (sum_nums + S) // 2
        dp = [0 for _ in range(need_sum + 1)]  # 前0个元素凑满n只有0种方法
        dp[0] = 1  # 前0个元素凑满0只有一种方法
        for num in nums:
            for total in range(need_sum, num - 1, -1):
                dp[total] += dp[total-num]
        return dp[need_sum]


# leetcode submit region end(Prohibit modification and deletion)

# if __name__ == '__main__':
#     # print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
#     print(Solution().findTargetSumWays([0,0,0,0,0,0,0,0,1], 1))
