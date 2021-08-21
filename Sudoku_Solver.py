# 20210821
# LeetCode

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def recurse(r, c):
            if r == 9: return True
            y, x = int(r), int(c) + 1
            if x == 9: y, x = y + 1, 0
            if board[r][c] != '.': return recurse(y, x)

            def valid():
                if digit in board[r]: return False
                for i in range(9):
                    if digit == board[i][c]: return False
                iul, jll = (r//3)*3, (c//3)*3
                ill, jrl = iul + 3, jll + 3
                for i in range(iul, ill):
                    for j in range(jll, jrl):
                        if digit == board[i][j]: return False
                return True

            for digit in "123456789":
                if valid():
                    board[r][c] = digit
                    if recurse(y, x) is True: return True
                    else: board[r][c] = '.'
            return False

        recurse(0, 0)

