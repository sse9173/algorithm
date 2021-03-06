# 20210523
# LeetCode

class Solution:
    ans = list()
    pos = list()
    size = 0
    def recurse(self, row):
        if row == self.size:
            board = list()
            for q in self.pos:
                board.append('.'*q + 'Q' + '.'*(self.size - q - 1))
            self.ans.append(board)
            return
        for i in range(self.size):
            if i in self.pos: continue
            flag = True
            for r in range(row):
                if (row - r) == abs(self.pos[r] - i):
                    flag = False
                    break
            if flag is True:
                self.pos[row] = i
                self.recurse(row + 1)
                self.pos[row] = -1
            
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ans.clear()
        self.pos = [-1 for i in range(n)]
        self.size = n
        self.recurse(0)
        return self.ans
