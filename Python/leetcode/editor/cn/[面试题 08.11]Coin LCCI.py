# Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 
# cents), and pennies (1 cent), write code to calculate the number of ways of 
# representing n cents. (The result may be large, so you should return it modulo 10000
# 00007) 
# 
#  Example1: 
# 
#  
#  Input: n = 5
#  Output: 2
#  Explanation: There are two ways:
# 5=5
# 5=1+1+1+1+1
#  
# 
#  Example2: 
# 
#  
#  Input: n = 10
#  Output: 4
#  Explanation: There are four ways:
# 10=10
# 10=5+5
# 10=5+1+1+1+1+1
# 10=1+1+1+1+1+1+1+1+1+1
#  
# 20=10+10
# 20=5+5+10=10+5+5
# 20=5+5+5+5
#
# 9=5+1+1+1+1
# 9=1+1+1+1+1+1+1+1+1+1
#  Notes:
# 
#  You can assume: 
# 
#  
#  0 <= n <= 1000000 
#  
# 
#  👍 293 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def waysToChange(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i][j] 表示前i个硬币构造等于j的方案数
        # dp[i][j] = dp[i][j-coins[i]] + dp[i-1][j]  第i个硬币用或不用
        dp = [[0] * (n + 1) for _ in range(5)]
        dp[0][0] = 1
        coins = [1, 5, 10, 25]
        for i in range(1, 5):
            for j in range(0, n + 1):
                c = coins[i - 1]
                # 第i个硬币用或不用
                dp[i][j] += (dp[i][j - c] if j >= c else 0) + dp[i - 1][j]
        # print(dp)
        return dp[4][n] % 1000000007

        # # 优化空间
        # dp = [0] * (n + 1)
        # dp[0] = 1
        # coins = [1, 5, 10, 25]
        # for i in range(1, 5):
        #     for j in range(0, n + 1):
        #         c = coins[i - 1]
        #         # 第i个硬币用或不用
        #         dp[j] = (dp[j - c] if j >= c else 0) + dp[j]
        # # print(dp)
        # return dp[n] % 1000000007


# leetcode submit region end(Prohibit modification and deletion)

# if __name__ == '__main__':
#     print(Solution().waysToChange(10))
#     print(Solution().waysToChange(5))
#     print(Solution().waysToChange(900750))
