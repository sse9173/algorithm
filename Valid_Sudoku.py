# 20210820
# LeetCode

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [list() for _ in range(9)]
        subs = [[list() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            rows = list()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in rows or board[i][j] in cols[j] or board[i][j] in subs[i//3][j//3]: return False
                    rows.append(board[i][j])
                    cols[j].append(board[i][j])
                    subs[i//3][j//3].append(board[i][j])
        return True
