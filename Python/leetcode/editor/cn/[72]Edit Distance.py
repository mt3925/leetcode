# Given two strings word1 and word2, return the minimum number of operations req
# uired to convert word1 to word2. 
# 
#  You have the following three operations permitted on a word: 
# 
#  
#  Insert a character 
#  Delete a character 
#  Replace a character 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
#  
# 
#  Example 2: 
# 
#  
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= word1.length, word2.length <= 500 
#  word1 and word2 consist of lowercase English letters. 
#  
#  Related Topics 字符串 动态规划 
#  👍 1516 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#
#         i = len(word1) - 1
#         j = len(word2) - 1
#
#         table = {}
#
#         def dp(i, j):
#             if (i, j) in table:
#                 return table[(i, j)]
#             if i < 0:
#                 return j + 1  # 不够的插入
#             if j < 0:
#                 return i + 1  # 多余的删除
#
#             if word1[i] == word2[j]:
#                 cnt = dp(i - 1, j - 1)
#
#             else:
#                 cnt = min(
#                     dp(i - 1, j) + 1,  # 删除
#                     dp(i - 1, j - 1) + 1,  # 替换
#                     dp(i, j - 1) + 1,  # 插入
#                 )
#             table[(i, j)] = cnt
#             return cnt
#         return dp(i, j)


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        len1 = len(word1)
        len2 = len(word2)
        if not len1:
            return len2
        if not len2:
            return len1

        dp = list(range(len2 + 1))

        for i in range(1, len1 + 1):
            left_prev, dp[0] = dp[0], i
            for j in range(1, len2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[j], left_prev = left_prev, dp[j]
                else:
                    dp[j], left_prev = min(
                        dp[j] + 1,  # 删除
                        dp[j - 1] + 1,  # 插入
                        left_prev + 1,  # 更新
                    ), dp[j]
        return dp[-1]


# leetcode submit region end(Prohibit modification and deletion)

# if __name__ == '__main__':
#     print(Solution().minDistance('horse', 'ros'))
#
# '''
#   ' h o r s e
# ' 0 1 2 3 4 5
# r 1 1 2 2 3 4
# o 2 2 1 2 3 4
# s 3 3 2 2 2 3
# '''
