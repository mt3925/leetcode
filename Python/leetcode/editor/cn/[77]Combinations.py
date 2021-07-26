# Given two integers n and k, return all possible combinations of k numbers out 
# of the range [1, n]. 
# 
#  You may return the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1, k = 1
# Output: [[1]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 20 
#  1 <= k <= n 
#  
#  Related Topics 数组 回溯 
#  👍 612 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        rst = []

        def backtrack(idx, path):
            for i in range(idx, n+1):
                path.append(i)
                if len(path) == k:
                    rst.append(path[:])
                else:
                    backtrack(i+1, path)
                path.pop()
        backtrack(1, [])
        return rst

# leetcode submit region end(Prohibit modification and deletion)
