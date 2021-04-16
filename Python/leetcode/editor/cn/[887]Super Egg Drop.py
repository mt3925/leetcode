# You are given k identical eggs and you have access to a building with n floors
#  labeled from 1 to n. 
# 
#  You know that there exists a floor f where 0 <= f <= n such that any egg drop
# ped at a floor higher than f will break, and any egg dropped at or below floor f
#  will not break. 
# 
#  Each move, you may take an unbroken egg and drop it from any floor x (where 1
#  <= x <= n). If the egg breaks, you can no longer use it. However, if the egg do
# es not break, you may reuse it in future moves. 
# 
#  Return the minimum number of moves that you need to determine with certainty 
# what the value of f is. 
# 
#  
#  Example 1: 
# 
#  
# Input: k = 1, n = 2
# Output: 2
# Explanation: 
# Drop the egg from floor 1. If it breaks, we know that f = 0.
# Otherwise, drop the egg from floor 2. If it breaks, we know that f = 1.
# If it does not break, then we know f = 2.
# Hence, we need at minimum 2 moves to determine with certainty what the value o
# f f is.
#  
# 
#  Example 2: 
# 
#  
# Input: k = 2, n = 6
# Output: 3
#  
# 
#  Example 3: 
# 
#  
# Input: k = 3, n = 14
# Output: 4
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= k <= 100 
#  1 <= n <= 104 
#  
#  Related Topics 数学 二分查找 动态规划 
#  👍 611 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# # 自底向上 暴力解法
# class Solution:
#     def superEggDrop(self, k: int, n: int) -> int:
#         '''
#           1 2 3 4 5 6 7 8 9
#         1 1 2 3 4 5 6 7 8 9
#         2 1 2 2 3 3 3 4 4 4
#         3 1 2 2 3 3 3 3 4 4
#         '''
#         dp = [[0] * (n + 1) for _ in range(k + 1)]
#         dp[1] = list(range(0, n + 1))
#         for i in range(2, k + 1):
#             for j in range(1, n + 1):
#                 step = j
#                 for s in range(j, 0, -1):
#                     step = min(step, max(
#                         dp[i-1][s-1] + 1,  # 碎了
#                         dp[i][j - s] + 1,  # 没碎
#                     ))
#                 dp[i][j] = step
#         return dp[k][n]


# # 自底向上 + 二分查找
# class Solution:
#     def superEggDrop(self, k: int, n: int) -> int:
#         '''
#           1 2 3 4 5 6 7 8 9
#         1 1 2 3 4 5 6 7 8 9
#         2 1 2 2 3 3 3 4 4 4
#         3 1 2 2 3 3 3 3 4 4
#         '''
#         dp_last = list(range(0, n + 1))
#         dp_cur = [0, 1] + [0] * (n - 1)
#
#         for i in range(2, k + 1):
#             for j in range(2, n + 1):
#                 left = 2
#                 right = j + 1
#                 while left < right:
#                     mid = (left + right) // 2
#                     t1 = dp_last[mid-1]
#                     t2 = dp_cur[j-mid]
#                     if t1 < t2:
#                         left = mid + 1
#                     elif t1 == t2:
#                         left = mid + 1
#                         right = mid + 1
#                     else:
#                         right = mid
#                 pos = left - 1
#                 dp_cur[j] = min(
#                     max(
#                         dp_last[pos-1] + 1,  # 碎了
#                         dp_cur[j-pos] + 1,  # 没碎
#                     ),
#                     max(
#                         dp_last[pos] + 1,  # 碎了
#                         dp_cur[j-pos-1] + 1,  # 没碎
#                     )
#                 )
#             dp_last = dp_cur
#             dp_cur = [0, 1] + [0] * (n - 1)
#         return dp_last[n]


# # 自顶向下 + 二分查找
# class Solution:
#     def superEggDrop(self, k: int, n: int) -> int:
#         memo = {}
#
#         def dp(k, n):
#             if (k, n) in memo:
#                 return memo[(k, n)]
#
#             if k == 1:
#                 rst = n
#             elif n <= 2:
#                 rst = n
#             else:
#                 left = 1
#                 right = n + 1
#                 while left < right:
#                     mid = (left + right) // 2
#                     t1 = dp(k - 1, mid - 1)
#                     t2 = dp(k, n - mid)
#                     if t1 < t2:
#                         left = mid + 1
#                     elif t1 == t2:
#                         left = mid + 1
#                         right = mid + 1
#                     else:
#                         right = mid
#                 pos = (left - 1) or 1
#                 rst = min(
#                     max(dp(k - 1, pos - 1), dp(k, n - pos)),
#                     max(dp(k - 1, pos), dp(k, n - pos - 1)),
#                 ) + 1
#             memo[(k, n)] = rst
#             return rst
#         return dp(k, n)


# # 自底向上 + 决策单调性
# class Solution:
#     def superEggDrop(self, k: int, n: int) -> int:
#         '''
#           1 2 3 4 5 6 7 8 9
#         1 1 2 3 4 5 6 7 8 9
#         2 1 2 2 3 3 3 4 4 4
#         3 1 2 2 3 3 3 3 4 4
#         dp(k,n)=1+ |1≤x≤n|min(max(dp(k−1,x−1),dp(k,n−x)))
#         固定 k，随着 n 的增加, dp(k−1,x−1)不变，dp(k,n−x)增加
#         固定k、n，dp(k,n−x)随x递减，所以n增加时 dp(k,n−x) 的下行折线整体右移
#         所以 最佳x的位置，也就是 dp(k−1,x−1) 和 dp(k,n−x) 的交点随着n增加而递增
#         '''
#         dp_last = list(range(0, n + 1))
#         dp_cur = [0, 1] + [0] * (n - 1)
#         for i in range(2, k + 1):
#             x = 2
#             for j in range(2, n + 1):
#                 while x <= j and dp_last[x - 1] <= dp_cur[j-x]:
#                     x += 1
#                 pos = x - 1
#                 dp_cur[j] = min(
#                     max(
#                         dp_last[pos-1] + 1,  # 碎了
#                         dp_cur[j-pos] + 1,  # 没碎
#                     ),
#                     max(
#                         dp_last[pos] + 1,  # 碎了
#                         dp_cur[j-pos-1] + 1,  # 没碎
#                     )
#                 )
#             dp_last = dp_cur[:]
#         return dp_last[n]


# 逆向思维
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        '''
          1 2 3 4 5 6 7 8 9
        1 1 2 3 4 5 6 7 8 9
        2 1 2 2 3 3 3 4 4 4
        3 1 2 2 3 3 3 3 4 4

        dp(c, k)=n  c代表扔的次数 n代表k个鸡蛋扔c次最多可以判断n层
        求最小的 c 使 dp(c, k) >= n
        '''

        dp = [0] * (k + 1)
        rst = 0
        for i in range(1, n + 1):
            for j in range(k, 0, -1):
                dp[j] = 1 + dp[j - 1] + dp[j]
            if dp[k] >= n:
                rst = i
                break
        return rst


# leetcode submit region end(Prohibit modification and deletion)

# if __name__ == '__main__':
#     print(Solution().superEggDrop(1, 2))   # 2
#     print(Solution().superEggDrop(2, 6))   # 3
#     print(Solution().superEggDrop(1, 2))   # 2
#     print(Solution().superEggDrop(2, 9))   # 4
#     print(Solution().superEggDrop(2, 7))   # 4
#     print(Solution().superEggDrop(3, 14))   # 4
#     print(Solution().superEggDrop(3, 4))   # 3
