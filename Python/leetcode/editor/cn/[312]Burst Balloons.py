# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted wit
# h a number on it represented by an array nums. You are asked to burst all the ba
# lloons. 
# 
#  If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1
# ] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if 
# there is a balloon with a 1 painted on it. 
# 
#  Return the maximum coins you can collect by bursting the balloons wisely. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
#  Example 2: 
# 
#  
# Input: nums = [1,5]
# Output: 10
#  
# 
#  
#  Constraints: 
# 
#  
#  n == nums.length 
#  1 <= n <= 500 
#  0 <= nums[i] <= 100 
#  
#  Related Topics 分治算法 动态规划 
#  👍 698 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        points = [1] + nums[:] + [1]
        cnt = len(points)

        dp = [[0] * cnt for _ in range(cnt)]

        # dp[i][j] 代表 第i到j个气球中间的气球最多可以获得的金币数 不包括i、j
        # 0-0 1-1 2-2 均为0
        for i in range(cnt - 2, -1, -1):
            for j in range(i + 1, cnt):
                # 选择一个气球作为最后戳破的气球
                coins = 0
                for opt in range(i + 1, j):
                    coins = max(coins, dp[i][opt] + dp[opt][j] + points[i] * points[opt] * points[j])
                dp[i][j] = coins
        return dp[0][-1]


# leetcode submit region end(Prohibit modification and deletion)

# if __name__ == '__main__':
#     print(Solution().maxCoins([3, 1, 5, 8]))
