# Given a collection of numbers, nums, that might contain duplicates, return all
#  possible unique permutations in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 8 
#  -10 <= nums[i] <= 10 
#  
#  Related Topics 数组 回溯 
#  👍 736 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#
#         rst = set()
#         cnt = len(nums)
#         used = [False] * cnt
#
#         def backtrack(nums, path):
#             if len(path) == cnt:
#                 rst.add(tuple(path[:]))
#                 return
#             for i in range(0, cnt):
#                 if used[i]:
#                     continue
#                 path.append(nums[i])
#                 used[i] = True
#                 backtrack(nums, path)
#                 path.pop()
#                 used[i] = False
#         backtrack(nums, [])
#         return [list(i) for i in rst]


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        rst = []
        choices = collections.Counter(nums)

        def backtrack(path):
            if len(path) == len(nums):
                rst.append(path[:])
                return

            for n, cnt in choices.items():
                if cnt <= 0:
                    continue
                path.append(n)
                choices[n] -= 1
                backtrack(path)
                choices[n] += 1
                path.pop()
        backtrack([])
        return rst

# leetcode submit region end(Prohibit modification and deletion)
