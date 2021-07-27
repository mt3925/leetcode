# Given an integer array nums and an integer k, return true if it is possible to
#  divide this array into k non-empty subsets whose sums are all equal. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,
# 3) with equal sums.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,2,3,4], k = 3
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= k <= nums.length <= 16 
#  1 <= nums[i] <= 104 
#  The frequency of each element is in the range [1, 4]. 
#  
#  Related Topics 位运算 记忆化搜索 数组 动态规划 回溯 状态压缩 
#  👍 374 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

# class Solution:
#     def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
#         _sum = sum(nums)
#         cnt = len(nums)
#         avg, rest = divmod(_sum, k)
#         if rest != 0:
#             return False
#
#         # nums.sort(reverse=True)
#         # buckets = [0] * k
#         #
#         # def backtrack(idx):
#         #     if idx >= cnt:
#         #         return all([i == avg for i in buckets])
#         #     for b_idx, bucket in enumerate(buckets):
#         #         if bucket + nums[idx] > avg:
#         #             continue
#         #         buckets[b_idx] += nums[idx]
#         #         if backtrack(idx+1):
#         #             return True
#         #         buckets[b_idx] -= nums[idx]
#         #     return False
#         # return backtrack(0)
#
#         buckets = [0] * k
#         nums.sort(reverse=True)
#
#         def backtrack(b_idx, idx, used):
#             if b_idx >= k:
#                 return True
#
#             for idx in range(idx, cnt):
#                 if idx in used:
#                     continue
#                 num = nums[idx]
#                 if buckets[b_idx] + num > avg:
#                     continue
#                 buckets[b_idx] += num
#                 used.add(idx)
#                 if buckets[b_idx] == avg:
#                     if backtrack(b_idx+1, 0, used):
#                         return True
#                 else:
#                     if backtrack(b_idx, idx+1, used):
#                         return True
#                 buckets[b_idx] -= num
#                 used.remove(idx)
#             return False
#         return backtrack(0, 0, set())


# class Solution:
#     def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
#         avg, rest = divmod(sum(nums), k)
#         if rest != 0:
#             return False
#         buckets = [0] * k
#         nums.sort(reverse=True)
#
#         def backtrack(idx):
#             if idx == len(nums):
#                 return True
#
#             for b_idx in range(0, k):
#                 if buckets[b_idx] + nums[idx] > avg:
#                     continue
#                 buckets[b_idx] += nums[idx]
#                 rst = backtrack(idx + 1)
#                 if rst:
#                     return True
#                 buckets[b_idx] -= nums[idx]
#             return False
#         return backtrack(0)


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        avg, rest = divmod(sum(nums), k)
        if rest != 0:
            return False
        nums.sort(reverse=True)
        buckets = [0] * k
        cnt = len(nums)

        def backtrack(b_idx, idx, choice):
            if len(choice) == cnt:
                return True
            if b_idx >= k:
                return False
            for idx in range(idx, cnt):
                if idx in choice:
                    continue
                n = nums[idx]
                if buckets[b_idx] + n > avg:
                    continue
                buckets[b_idx] += n
                choice.add(idx)
                if buckets[b_idx] == avg:
                    if backtrack(b_idx + 1, 0, choice):
                        return True
                else:
                    if backtrack(b_idx, idx + 1, choice):
                        return True
                choice.remove(idx)
                buckets[b_idx] -= n
            return False
        return backtrack(0, 0, set())

# leetcode submit region end(Prohibit modification and deletion)
