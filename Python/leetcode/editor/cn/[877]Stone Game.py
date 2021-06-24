# Alex and Lee play a game with piles of stones. There are an even number of pil
# es arranged in a row, and each pile has a positive integer number of stones pile
# s[i]. 
# 
#  The objective of the game is to end with the most stones. The total number of
#  stones is odd, so there are no ties. 
# 
#  Alex and Lee take turns, with Alex starting first. Each turn, a player takes 
# the entire pile of stones from either the beginning or the end of the row. This 
# continues until there are no more piles left, at which point the person with the
#  most stones wins. 
# 
#  Assuming Alex and Lee play optimally, return True if and only if Alex wins th
# e game. 
# 
#  
#  Example 1: 
# 
#  
# Input: piles = [5,3,4,5]
# Output: true
# Explanation: 
# Alex starts first, and can only take the first 5 or the last 5.
# Say he takes the first 5, so that the row becomes [3, 4, 5].
# If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 poin
# ts.
# If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win wit
# h 9 points.
# This demonstrated that taking the first 5 was a winning move for Alex, so we r
# eturn true.
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= piles.length <= 500 
#  piles.length is even. 
#  1 <= piles[i] <= 500 
#  sum(piles) is odd. 
#  
#  Related Topics 极小化极大 数学 动态规划 
#  👍 235 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        cnt = len(piles)
        dp = [[(0, 0)] * cnt for _ in range(cnt)]
        # i j 代表 下标i到j之间的石堆 先手最大石子数，后手最大石子数
        for i in range(cnt):
            dp[i][i] = (piles[i], 0)

        for delta in range(1, cnt):
            for i in range(cnt - delta):
                j = i + delta

                left = piles[i] + dp[i + 1][j][1]
                right = piles[j] + dp[i][j - 1][1]
                if left > right:
                    fir = left
                    sec = dp[i+1][j][0]
                else:
                    fir = right
                    sec = dp[i][j - 1][0]
                dp[i][j] = (fir, sec)
        return dp[0][cnt - 1][0] > dp[0][cnt - 1][1]



# leetcode submit region end(Prohibit modification and deletion)
