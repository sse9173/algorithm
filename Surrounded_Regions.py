# 20211101
# LeetCode

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def recurse(y, x):
            nonlocal board, m, n
            board[y][x] = '.'
            if y > 0 and board[y - 1][x] == 'O': recurse(y - 1, x)
            if x < n - 1 and board[y][x + 1] == 'O': recurse(y, x + 1)
            if y < m - 1 and board[y + 1][x] == 'O': recurse(y + 1, x)
            if x > 0 and board[y][x - 1] == 'O': recurse(y, x - 1)

        for i in range(m):
            if board[i][0] == 'O': recurse(i, 0)
            if board[i][n - 1] == 'O': recurse(i, n - 1)
        for j in range(n):
            if board[0][j] == 'O': recurse(0, j)
            if board[m - 1][j] == 'O': recurse(m - 1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O': board[i][j] = 'X'
                elif board[i][j] == '.': board[i][j] = 'O'

