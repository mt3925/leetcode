# Given two strings word1 and word2, return the minimum number of steps required
#  to make word1 and word2 the same. 
# 
#  In one step, you can delete exactly one character in either string. 
# 
#  
#  Example 1: 
# 
#  
# Input: word1 = "sea", word2 = "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make
# "eat" to "ea".
#  
# 
#  Example 2: 
# 
#  
# Input: word1 = "leetcode", word2 = "etco"
# Output: 4
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= word1.length, word2.length <= 500 
#  word1 and word2 consist of only lowercase English letters. 
#  
#  Related Topics 字符串 
#  👍 183 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = list(range(len(word2) + 1))
        for i in range(1, len(word1) + 1):
            prev = i - 1
            dp[0] = i
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    dp[j], prev = prev, dp[j]
                else:
                    dp[j], prev = min(dp[j] + 1, dp[j-1] + 1), dp[j]
        return dp[-1]

# leetcode submit region end(Prohibit modification and deletion)
