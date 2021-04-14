# Given an integer array nums, find the contiguous subarray (containing at least
#  one number) which has the largest sum and return its sum. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1]
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [5,4,-1,7,8]
# Output: 23
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 3 * 104 
#  -105 <= nums[i] <= 105 
#  
# 
#  
# Follow up: If you have figured out the O(n) solution, try coding another solut
# ion using the divide and conquer approach, which is more subtle. Related Topics 
# 数组 分治算法 动态规划 
#  👍 3109 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         last = rst = nums[0]
#         for i in range(1, len(nums)):
#             last = max(nums[i], last + nums[i])
#             rst = max(last, rst)
#         return rst


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        class Status:
            def __init__(self, lsum, rsum, isum, msum):
                self.lsum = lsum
                self.rsum = rsum
                self.isum = isum
                self.msum = msum

            def __add__(self, other):
                isum = self.isum + other.isum
                lsum = max(self.lsum, self.isum + other.lsum)
                rsum = max(other.rsum, self.rsum + other.isum)
                msum = max((self.msum, other.msum, self.rsum + other.lsum))
                return Status(lsum, rsum, isum, msum)

        def get(start, end):
            if start == end:
                return Status(nums[start], nums[start], nums[start], nums[start])
            mid = (start + end) // 2
            left = get(start, mid)
            right = get(mid + 1, end)
            return left + right
        return get(0, len(nums) - 1).msum


# leetcode submit region end(Prohibit modification and deletion)
