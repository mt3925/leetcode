# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
# 
#  示例 2: 
# 
#  
# 输入: n = 1, k = 1
# 输出: [[1]] 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= n <= 20 
#  1 <= k <= n 
#  
# 
#  
# 
#  
#  注意：本题与主站 77 题相同： https://leetcode-cn.com/problems/combinations/ 
# 
#  Related Topics 数组 回溯 👍 64 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        all_rst = []

        def backtrack(rst, start=1):
            if len(rst) == k:
                all_rst.append([i for i in rst])
                return

            for i in range(start, n + 1):
                if i in rst:
                    continue
                rst.append(i)
                backtrack(rst, start=i + 1)
                rst.pop()
        backtrack([])
        return all_rst

# leetcode submit region end(Prohibit modification and deletion)


# if __name__ == '__main__':
#     n = 4
#     k = 2
#     print(Solution().combine(n, k))
