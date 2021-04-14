# Given a non-empty array nums containing only positive integers, find if the ar
# ray can be partitioned into two subsets such that the sum of elements in both su
# bsets is equal. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 200 
#  1 <= nums[i] <= 100 
#  
#  Related Topics 动态规划 
#  👍 746 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False
        total, remain = divmod(sum(nums), 2)
        if remain:
            return False

        dp = [True] + [False] * total
        for i in range(1, len(nums) + 1):
            for j in range(total, 0, -1):
                if j >= nums[i - 1]:
                    dp[j] = dp[j] or dp[j - nums[i - 1]]
        return dp[-1]


# leetcode submit region end(Prohibit modification and deletion)
