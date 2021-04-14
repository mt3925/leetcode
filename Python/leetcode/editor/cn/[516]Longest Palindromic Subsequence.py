# Given a string s, find the longest palindromic subsequence's length in s. 
# 
#  A subsequence is a sequence that can be derived from another sequence by dele
# ting some or no elements without changing the order of the remaining elements. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 1000 
#  s consists only of lowercase English letters. 
#  
#  Related Topics 动态规划 
#  👍 421 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         len_s = len(s)
#         if len_s <= 1 or s == s[::-1]:
#             return len_s
#         dp = [0] * (len_s + 1)
#         for i in range(1, len_s + 1):
#             left_prev = 0
#             for j in range(1, len_s + 1):
#                 if s[i - 1] == s[-j]:
#                     dp[j], left_prev = left_prev + 1, dp[j]
#                 else:
#                     dp[j], left_prev = max(
#                         dp[j - 1],
#                         dp[j],
#                     ), dp[j]
#         return dp[-1]

# # 斜着遍历
# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         len_s = len(s)
#         if len_s <= 1 or s == s[::-1]:
#             return len_s
#
#         dp = [[0] * len_s for _ in range(len_s)]
#         for i in range(len_s):
#             dp[i][i] = 1
#
#         for delta in range(1, len_s):
#             for i in range(0, len_s - delta):
#                 j = i + delta
#                 if s[i] == s[j]:
#                     dp[i][j] = dp[i + 1][j - 1] + 2
#                 else:
#                     dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
#         return dp[0][len_s - 1]


# 倒序遍历
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        len_s = len(s)
        if len_s <= 1 or s == s[::-1]:
            return len_s

        dp = [1] * len_s
        for j in range(1, len_s):
            prev = 0
            for i in range(j - 1, -1, -1):
                if s[i] == s[j]:
                    dp[i], prev = prev + 2, dp[i]
                else:
                    dp[i], prev = max(dp[i + 1], dp[i]), dp[i]
        return dp[0]

# leetcode submit region end(Prohibit modification and deletion)
#
# '''
#   b b b a b
#   0 1 2 3 4
# 0 1 2 3 3 4
# 1   1 2 2 3
# 2     1 1 2
# 3       1 1
# 4         1
#
# '''
# if __name__ == '__main__':
#     print(Solution().longestPalindromeSubseq('bbbab'))

