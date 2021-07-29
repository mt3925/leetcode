# Given an array of positive integers nums and a positive integer target, return
#  the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, nums
# r] of which the sum is greater than or equal to target. If there is no such suba
# rray, return 0 instead. 
# 
#  
#  Example 1: 
# 
#  
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem const
# raint.
#  
# 
#  Example 2: 
# 
#  
# Input: target = 4, nums = [1,4,4]
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= target <= 109 
#  1 <= nums.length <= 105 
#  1 <= nums[i] <= 105 
#  
# 
#  
# Follow up: If you have figured out the O(n) solution, try coding another solut
# ion of which the time complexity is O(n log(n)). Related Topics 数组 二分查找 前缀和 滑动窗口
#  
#  👍 702 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
# leetcode submit region end(Prohibit modification and deletion)
