# 
# Given a list of daily temperatures T, return a list such that, for each day in
#  the input, tells you how many days you would have to wait until a warmer temper
# ature. If there is no future day for which this is possible, put 0 instead.
#  
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 7
# 3], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
#  
# 
#  Note:
# The length of temperatures will be in the range [1, 30000].
# Each temperature will be an integer in the range [30, 100].
#  Related Topics 栈 哈希表 
#  👍 676 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        rst = [0] * len(T)
        stack = []
        for idx, item in enumerate(T):
            while stack and item > T[stack[-1]]:
                cur = stack.pop()
                rst[cur] = idx - cur
            stack.append(idx)
        return rst

#
# class Solution:
#     def dailyTemperatures(self, T):
#         ans = [0] * len(T)
#         stack = []
#         for i, t in enumerate(T):
#             while stack and T[stack[-1]] < t:
#                 cur = stack.pop()
#                 ans[cur] = i - cur
#             stack.append(i)
#         return ans


# class Solution:
#     def dailyTemperatures(self, T: List[int]) -> List[int]:
#         n, right_max = len(T), float('-inf')
#         res = [0] * n
#         for i in range(n-1, -1, -1):
#             t = T[i]
#             if right_max <= t:
#                 right_max = t
#             else:
#                 days = 1
#                 while T[i+days] <= t:
#                     days += res[i+days]
#                 res[i] = days
#         return res
# leetcode submit region end(Prohibit modification and deletion)
