# Given an array nums of n integers and an integer target, are there elements a,
#  b, c, and d in nums such that a + b + c + d = target? Find all unique quadruple
# ts in the array which gives the sum of target. 
# 
#  Notice that the solution set must not contain duplicate quadruplets. 
# 
#  
#  Example 1: 
#  Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#  Example 2: 
#  Input: nums = [], target = 0
# Output: []
#  
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 200 
#  -109 <= nums[i] <= 109 
#  -109 <= target <= 109 
#  
#  Related Topics 数组 哈希表 双指针 
#  👍 774 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         if len(nums) < 4:
#             return []
#         rst = []
#         nums.sort()
#         for idx1, item1 in enumerate(nums[:-3]):
#             if idx1 >= 1 and nums[idx1 - 1] == item1:
#                 continue
#             for idx2, item2 in enumerate(nums[idx1 + 1:], start=idx1 + 1):
#                 if idx2 > idx1 + 1 and nums[idx2 - 1] == item2:
#                     continue
#                 remain_map = {}
#                 for idx3, item3 in enumerate(nums[idx2 + 1:], start=idx2 + 1):
#                     if item3 in remain_map and remain_map[item3] == 0:
#                         rst.append([item1, item2, target - item1 - item2 - item3, item3])
#                         remain_map[item3] += 1
#                     remain = target - item1 - item2 - item3
#                     remain_map.setdefault(remain, 0)
#         return rst


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        len_nums = len(nums)

        # hash后两个数的和，并保存索引
        table = {}
        for j in range(len_nums-1, 2, -1):
            if j < len_nums-1 and nums[j] == nums[j+1]:
                continue
            if 4 * nums[j] < target:
                break
            if nums[j] + 3*nums[0] > target:
                continue
            for i in range(j-1, 1, -1):
                if i < j-1 and nums[i] == nums[i+1]:
                    continue
                if nums[j] + 3*nums[i] < target:
                    break
                if nums[j] + nums[i] + 2*nums[0] > target:
                    continue
                table.setdefault(nums[i] + nums[j], []).append((i, j))

        # 枚举前两个数
        for i in range(len_nums-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] * 4 > target:
                break
            if nums[i] + 3 * nums[-1] < target:
                continue
            for j in range(i + 1, len_nums-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + 3*nums[j] > target:
                    break
                if nums[i] + nums[j] + 2*nums[-1] < target:
                    continue
                for index, jndex in table.get(target - nums[i] - nums[j], []):
                    if j < index:
                        ans.append([nums[i], nums[j], nums[index], nums[jndex]])

        return ans

# leetcode submit region end(Prohibit modification and deletion)
