# Given two strings text1 and text2, return the length of their longest common s
# ubsequence. If there is no common subsequence, return 0. 
# 
#  A subsequence of a string is a new string generated from the original string 
# with some characters (can be none) deleted without changing the relative order o
# f the remaining characters. 
# 
#  
#  For example, "ace" is a subsequence of "abcde". 
#  
# 
#  A common subsequence of two strings is a subsequence that is common to both s
# trings. 
# 
#  
#  Example 1: 
# 
#  
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
#  
# 
#  Example 2: 
# 
#  
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
#  
# 
#  Example 3: 
# 
#  
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= text1.length, text2.length <= 1000 
#  text1 and text2 consist of only lowercase English characters. 
#  
#  Related Topics 动态规划 
#  👍 508 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [0] * (len(text2) + 1)
        for i in range(1, len(text1) + 1):
            left_prev = 0
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[j], left_prev = left_prev + 1, dp[j]
                else:
                    dp[j], left_prev = max(dp[j-1], dp[j]), dp[j]
        return dp[-1]


# leetcode submit region end(Prohibit modification and deletion)
