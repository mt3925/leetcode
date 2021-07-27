# Given an array nums of distinct integers, return all the possible permutations
# . You can return the answer in any order. 
# 
#  
#  Example 1: 
#  Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  Example 2: 
#  Input: nums = [0,1]
# Output: [[0,1],[1,0]]
#  Example 3: 
#  Input: nums = [1]
# Output: [[1]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 6 
#  -10 <= nums[i] <= 10 
#  All the integers of nums are unique. 
#  
#  Related Topics 回溯算法 
#  👍 1310 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#
#         rst = []
#
#         def backtrack(path, choices):
#             if not choices:
#                 rst.append(path[:])
#                 return
#
#             for num in list(choices):
#                 choices.remove(num)
#                 path.append(num)
#                 backtrack(path, choices)
#                 path.pop()
#                 choices.add(num)
#         backtrack([], set(nums))
#         return rst

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        rst = []

        def backtrack(path, choices):
            if not choices:
                rst.append(path[:])
                return
            for n in list(choices):
                choices.remove(n)
                path.append(n)
                backtrack(path, choices)
                path.pop()
                choices.add(n)
        backtrack([], set(nums))
        return rst

# leetcode submit region end(Prohibit modification and deletion)
