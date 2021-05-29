# 20210530
# LeetCode

class Solution:
    cnt = 0
    size = 0
    pos = list()
    def recurse(self, row):
        if row == self.size:
            self.cnt += 1
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
    def totalNQueens(self, n: int) -> int:
        self.cnt = 0
        self.size = n
        self.pos = [-1 for i in range(n)]
        self.recurse(0)
        return self.cnt
