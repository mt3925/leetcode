# Given an integer array nums, return the length of the longest strictly increas
# ing subsequence. 
# 
#  A subsequence is a sequence that can be derived from an array by deleting som
# e or no elements without changing the order of the remaining elements. For examp
# le, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7]. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the 
# length is 4.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,1,0,3,2,3]
# Output: 4
#
# 
#  Example 3: 
# 
#  
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2500 
#  -104 <= nums[i] <= 104 
#  
# 
#  
#  Follow up: 
# 
#  
#  Could you come up with the O(n2) solution? 
#  Could you improve it to O(n log(n)) time complexity? 
#  
#  Related Topics 二分查找 动态规划 
#  👍 1510 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        rst = [nums[0]]
        for num in nums[1:]:
            if num > rst[-1]:
                rst.append(num)
            else:
                rst[bisect.bisect_left(rst, num)] = num
        return len(rst)


# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         len_nums = len(nums)
#
#         dp = [1] * len_nums
#         for i in range(1, len_nums):
#             cnt = 1
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     cnt = max(cnt, dp[j] + 1)
#             dp[i] = cnt
#         return max(dp)


# leetcode submit region end(Prohibit modification and deletion)
