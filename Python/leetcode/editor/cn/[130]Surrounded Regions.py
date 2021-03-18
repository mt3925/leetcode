# Given an m x n matrix board containing 'X' and 'O', capture all regions surrou
# nded by 'X'. 
# 
#  A region is captured by flipping all 'O's into 'X's in that surrounded region
# . 
# 
#  
#  Example 1: 
# 
#  
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O"
# ,"X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X
# "]]
# Explanation: Surrounded regions should not be on the border, which means that 
# any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not o
# n the border and it is not connected to an 'O' on the border will be flipped to 
# 'X'. Two cells are connected if they are adjacent cells connected horizontally o
# r vertically.
#  
# 
#  Example 2: 
# 
#  
# Input: board = [["X"]]
# Output: [["X"]]
#  
# 
#  
#  Constraints: 
# 
#  
#  m == board.length 
#  n == board[i].length 
#  1 <= m, n <= 200 
#  board[i][j] is 'X' or 'O'. 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 
#  👍 481 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        m = len(board)
        n = len(board[0])
        if n == 0:
            return

        def dfs(x, y):
            board[x][y] = '#'
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = x + dx
                ny = y + dy
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                if board[nx][ny] == 'O':
                    dfs(nx, ny)

        for idx in range(n):
            if board[0][idx] == 'O':
                dfs(0, idx)
            if board[-1][idx] == 'O':
                dfs(m - 1, idx)
        for idx in range(m):
            if board[idx][0] == 'O':
                dfs(idx, 0)
            if board[idx][-1] == 'O':
                dfs(idx, n - 1)

        for x in range(m):
            for y in range(n):
                if board[x][y] == '#':
                    board[x][y] = 'O'
                elif board[x][y] == 'O':
                    board[x][y] = 'X'
        return

# leetcode submit region end(Prohibit modification and deletion)
