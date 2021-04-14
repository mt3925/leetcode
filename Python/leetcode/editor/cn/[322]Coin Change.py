# You are given an integer array coins representing coins of different denominat
# ions and an integer amount representing a total amount of money. 
# 
#  Return the fewest number of coins that you need to make up that amount. If th
# at amount of money cannot be made up by any combination of the coins, return -1.
#  
# 
#  You may assume that you have an infinite number of each kind of coin. 
# 
#  
#  Example 1: 
# 
#  
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#  
# 
#  Example 2: 
# 
#  
# Input: coins = [2], amount = 3
# Output: -1
#  
# 
#  Example 3: 
# 
#  
# Input: coins = [1], amount = 0
# Output: 0
#  
# 
#  Example 4: 
# 
#  
# Input: coins = [1], amount = 1
# Output: 1
#  
# 
#  Example 5: 
# 
#  
# Input: coins = [1], amount = 2
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= coins.length <= 12 
#  1 <= coins[i] <= 231 - 1 
#  0 <= amount <= 104 
#  
#  Related Topics 动态规划 
#  👍 1150 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#
#         dp_table = {}
#
#         def dp(n):
#             if n in dp_table:
#                 return dp_table[n]
#             if n == 0:
#                 return 0
#             if n < 0:
#                 return -1
#             cnt = float('INF')
#             for coin in coins:
#                 other_cnt = dp(n - coin)
#                 if other_cnt == -1:
#                     continue
#                 cnt = min(cnt, 1 + other_cnt)
#             dp_table[n] = cnt
#             return -1 if cnt == float('INF') else cnt
#         return dp(amount)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for n in range(1, amount + 1):
            for coin in coins:
                if n - coin >= 0:
                    dp[n] = min(dp[n], 1 + dp[n - coin])
        return dp[amount] if dp[amount] < (amount + 1) else -1


# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         min_cnt = float('inf')
#         coins.sort(reverse=True)
#         len_coins = len(coins)
#
#         def dp(idx, coin_cnt, remain_amount):
#             nonlocal min_cnt
#             if remain_amount == 0:
#                 min_cnt = min(min_cnt, coin_cnt)
#                 return
#             for i in range(idx, len_coins):
#                 remain_coin_cnt = min_cnt - coin_cnt
#                 max_amount = coins[i] * remain_coin_cnt
#                 if coins[i] <= remain_amount < max_amount:
#                     dp(i, coin_cnt + 1, remain_amount - coins[i])
#
#         dp(0, 0, amount)
#         return min_cnt if min_cnt != float('inf') else -1


# leetcode submit region end(Prohibit modification and deletion)
#
# if __name__ == '__main__':
#     # print(Solution().coinChange([1, 2, 5], 11))
#     print(Solution().coinChange([186,419,83,408], 6249))
