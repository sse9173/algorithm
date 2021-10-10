# 20211007
# LeetCode

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        v = [[False for _ in range(n)] for _ in range(m)]

        def promising(y, x, widx):
            if widx == len(word): return True
            if y > 0 and v[y - 1][x] is False and board[y - 1][x] == word[widx]:
                v[y - 1][x] = True
                if promising(y - 1, x, widx + 1) is True: return True
                v[y - 1][x] = False
            if x + 1 < n and v[y][x + 1] is False and board[y][x + 1] == word[widx]:
                v[y][x + 1] = True
                if promising(y, x + 1, widx + 1) is True: return True
                v[y][x + 1] = False
            if y + 1 < m and v[y + 1][x] is False and board[y + 1][x] == word[widx]:
                v[y + 1][x] = True
                if promising(y + 1, x, widx + 1) is True: return True
                v[y + 1][x] = False
            if x > 0 and v[y][x - 1] is False and board[y][x - 1] == word[widx]:
                v[y][x - 1] = True
                if promising(y, x - 1, widx + 1) is True: return True
                v[y][x - 1] = False
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    v[i][j] = True
                    if promising(i, j, 1) is True: return True
                    v[i][j] = False
        return False
