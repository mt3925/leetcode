# Given two strings s1, s2, find the lowest ASCII sum of deleted characters to m
# ake two strings equal. 
# 
#  Example 1: 
#  
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the 
# sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum pos
# sible to achieve this.
#  
#  
# 
#  Example 2: 
#  
# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to
#  the sum.
# At the end, both strings are equal to "let", and the answer is 100+101+101+101
#  = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers of
#  433 or 417, which are higher.
#  
#  
# 
#  Note:
#  0 < s1.length, s2.length <= 1000. 
#  All elements of each string will have an ASCII value in [97, 122]. 
#  Related Topics 动态规划 
#  👍 211 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [0] * (len(s2) + 1)

        left_prev = 0
        for i in range(0, len(s1) + 1):
            for j in range(0, len(s2) + 1):
                if i == 0:
                    if j >= 1:
                        dp[j] = ord(s2[j - 1]) + dp[j - 1]
                elif j == 0:
                    if i >= 1:
                        dp[j], left_prev = ord(s1[i - 1]) + dp[j], dp[j]
                else:
                    if s1[i - 1] == s2[j - 1]:
                        dp[j], left_prev = left_prev, dp[j]
                    else:
                        dp[j], left_prev = min(dp[j] + ord(s1[i - 1]), dp[j - 1] + ord(s2[j - 1])), dp[j]
        return dp[-1]


# leetcode submit region end(Prohibit modification and deletion)
