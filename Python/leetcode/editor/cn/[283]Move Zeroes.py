# Given an integer array nums, move all 0's to the end of it while maintaining t
# he relative order of the non-zero elements. 
# 
#  Note that you must do this in-place without making a copy of the array. 
# 
#  
#  Example 1: 
#  Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#  Example 2: 
#  Input: nums = [0]
# Output: [0]
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 104 
#  -231 <= nums[i] <= 231 - 1 
#  
# 
#  
# Follow up: Could you minimize the total number of operations done? Related Top
# ics 数组 双指针 
#  👍 996 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     slow = fast = 0
    #     while fast < len(nums):
    #         if nums[fast] != 0:
    #             if fast != slow:
    #                 nums[slow], nums[fast] = nums[fast], 0
    #             slow += 1
    #         fast += 1

    def moveZeroes(self, nums: List[int]) -> None:
        slow = fast = 0

        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1

# leetcode submit region end(Prohibit modification and deletion)
