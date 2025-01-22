# 如果一个二进制字符串，是以一些 0（可能没有 0）后面跟着一些 1（也可能没有 1）的形式组成的，那么该字符串是 单调递增 的。 
# 
#  给你一个二进制字符串 s，你可以将任何 0 翻转为 1 或者将 1 翻转为 0 。 
# 
#  返回使 s 单调递增的最小翻转次数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "00110"
# 输出：1
# 解释：翻转最后一位得到 00111.
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "010110"
# 输出：2
# 解释：翻转得到 011111，或者是 000111。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "00011000"
# 输出：2
# 解释：翻转得到 00000000。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s[i] 为 '0' 或 '1' 
#  
# 
#  Related Topics 字符串 动态规划 👍 366 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """

        # dp[i][0] = dp[i - 1][0] + (s[i - 1] == '1')   下标i处为0的前缀串s[:i+1]最少翻转次数
        # dp[i][1] = min(dp[i - 1][1], dp[i - 1][0]) + (s[i - 1] == '0')   下标i处为1的前缀串s[:i+1]最少翻转次数
        # dp = [[0, 0] for _ in range(len(s))]
        # if s[0] == '0':
        #     dp[0][1] = 1
        # else:
        #     dp[0][0] = 1
        # for i in range(1, len(s)):
        #     if s[i] == '0':
        #         dp[i][0] = dp[i - 1][0]
        #         dp[i][1] = min(dp[i - 1]) + 1
        #     else:
        #         dp[i][0] = dp[i - 1][0] + 1
        #         dp[i][1] = min(dp[i - 1])
        # return min(dp[-1])

        dp0, dp1 = 0, 0
        for c in s:
            if c == '0':
                dp1 = min(dp0, dp1) + 1
            else:
                dp1 = min(dp0, dp1)
                dp0 += 1
        return min(dp0, dp1)
        
# leetcode submit region end(Prohibit modification and deletion)
