# Given an array nums of n integers, are there elements a, b, c in nums such tha
# t a + b + c = 0? Find all unique triplets in the array which gives the sum of ze
# ro. 
# 
#  Notice that the solution set must not contain duplicate triplets. 
# 
#  
#  Example 1: 
#  Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#  Example 2: 
#  Input: nums = []
# Output: []
#  Example 3: 
#  Input: nums = [0]
# Output: []
#  
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 3000 
#  -105 <= nums[i] <= 105 
#  
#  Related Topics 数组 双指针 
#  👍 3101 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         rst = []
#         right = len(nums) - 1
#         last_item = None
#         for idx, item in enumerate(nums):
#             if item == last_item:
#                 continue
#             others = two_sum(0 - item, nums, left=idx + 1, right=right)
#             for other in others:
#                 rst.append([item, *other])
#             last_item = item
#         return rst
#
#
# def two_sum(target, nums, left, right):
#     rst = []
#     last_left = None
#     last_right = None
#     # 0 1 2
#     while left < right:
#         if nums[left] == last_left:
#             left += 1
#             continue
#         if nums[right] == last_right:
#             right -= 1
#             continue
#         total = nums[left] + nums[right]
#         if total == target:
#             rst.append((nums[left], nums[right]))
#             last_left = nums[left]
#             last_right = nums[right]
#             left += 1
#             right -= 1
#         elif total > target:
#             last_right = nums[right]
#             right -= 1
#         else:
#             last_left = nums[left]
#             left += 1
#     return rst
import bisect
import collections
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        cnt_map = collections.Counter(nums)
        rst = []
        vals = sorted(cnt_map.keys())
        for idx, item in enumerate(vals):
            if cnt_map[item] >= 2:
                if item == 0 and cnt_map[0] >= 3:
                    rst.append([0, 0, 0])
                if item != 0 and cnt_map[-2 * item] > 0:
                    rst.append([item, item, -2 * item])

            if item < 0:
                rest = -item

                left = bisect.bisect_left(vals, rest - vals[-1], lo=idx + 1)
                right = bisect.bisect_right(vals, rest // 2, lo=left)
                for item2 in vals[left:right]:
                    item3 = rest - item2
                    if item3 in cnt_map and item3 != item2:
                        rst.append([item, item2, item3])
        return rst

# leetcode submit region end(Prohibit modification and deletion)

# if __name__ == '__main__':
#     print(Solution().threeSum([-1,0,1,2,-1,-4]))
