# Given n pairs of parentheses, write a function to generate all combinations of
#  well-formed parentheses. 
# 
#  
#  Example 1: 
#  Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
#  Example 2: 
#  Input: n = 1
# Output: ["()"]
#  
#  
#  Constraints: 
# 
#  
#  1 <= n <= 8 
#  
#  Related Topics 字符串 动态规划 回溯 
#  👍 1852 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        rst = []

        def backtrack(path, left, right):
            if right < left:
                return
            if left < 0 or right < 0:
                return
            if left == 0 and right == 0:
                rst.append(''.join(path))
                return

            path.append('(')
            backtrack(path, left-1, right)
            path.pop()

            path.append(')')
            backtrack(path, left, right - 1)
            path.pop()

        backtrack([], n, n)
        return rst


# leetcode submit region end(Prohibit modification and deletion)
