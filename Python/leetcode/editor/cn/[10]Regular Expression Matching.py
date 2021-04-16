# Given an input string (s) and a pattern (p), implement regular expression matc
# hing with support for '.' and '*' where: 
# 
#  
#  '.' Matches any single character. 
#  '*' Matches zero or more of the preceding element. 
#  
# 
#  The matching should cover the entire input string (not partial). 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, 
# by repeating 'a' once, it becomes "aa".
#  
# 
#  Example 3: 
# 
#  
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
#  
# 
#  Example 4: 
# 
#  
# Input: s = "aab", p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, i
# t matches "aab".
#  
# 
#  Example 5: 
# 
#  
# Input: s = "mississippi", p = "mis*is*p*."
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= s.length <= 20 
#  0 <= p.length <= 30 
#  s contains only lowercase English letters. 
#  p contains only lowercase English letters, '.', and '*'. 
#  It is guaranteed for each appearance of the character '*', there will be a pr
# evious valid character to match. 
#  
#  Related Topics 字符串 动态规划 回溯算法 
#  👍 2042 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] != '*':
                    if s[i-1] == p[j-1] or p[j-1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j-2] or dp[i][j-1] or (
                            (s[i-1] == s[i-2] and s[i-1] == p[j-2] or p[j-2] == '.') and dp[i-1][j])
        return dp[-1][-1]

# leetcode submit region end(Prohibit modification and deletion)

#
# if __name__ == '__main__':
#     # print(Solution().isMatch('aa', 'a*'))
#     print(Solution().isMatch('a', '.*..a*'))
