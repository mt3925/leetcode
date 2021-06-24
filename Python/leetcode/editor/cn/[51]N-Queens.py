# The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
# such that no two queens attack each other. 
# 
#  Given an integer n, return all distinct solutions to the n-queens puzzle. 
# 
#  Each solution contains a distinct board configuration of the n-queens' placem
# ent, where 'Q' and '.' both indicate a queen and an empty space, respectively. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as show
# n above
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1
# Output: [["Q"]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 9 
#  
#  Related Topics 回溯算法 
#  👍 846 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [['.'] * n for _ in range(n)]

        rst = []

        def backtrack(row):
            if row >= n:
                rst.append([''.join(i) for i in board])
                return

            for col in range(n):
                if not is_valid(row, col):
                    continue
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

        def is_valid(row, col):
            # 判断 当前列是否满足
            for r in range(row):
                if board[r][col] == 'Q':
                    return False
            # 判断左上是否满足
            c = col
            for r in range(row - 1, -1, -1):
                c -= 1
                if c < 0:
                    break
                if board[r][c] == 'Q':
                    return False
            # 判断右上
            c = col
            for r in range(row - 1, -1, -1):
                c += 1
                if c >= n:
                    break
                if board[r][c] == 'Q':
                    return False
            return True

        backtrack(0)
        return rst

# leetcode submit region end(Prohibit modification and deletion)
