# 20210909
# LeetCode

# Not Optimized
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        if len(mines) == n*n: return 0
        l = [[1 for j in range(n)] for i in range(n)]
        u = [[1 for j in range(n)] for i in range(n)]
        r = [[1 for j in range(n)] for i in range(n)]
        d = [[1 for j in range(n)] for i in range(n)]
        for i, j in mines: l[i][j], u[i][j], r[i][j], d[i][j] = 0, 0, 0, 0
        for i in range(1, n):
            for j in range(1, n):
                if l[i][j] != 0: l[i][j] += l[i][j - 1]
                if u[i][j] != 0: u[i][j] += u[i - 1][j]
        for i in range(n - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if r[i][j] != 0: r[i][j] += r[i][j + 1]
                if d[i][j] != 0: d[i][j] += d[i + 1][j]
        ret = 1
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                ret = max(ret, min(l[i][j], u[i][j], r[i][j], d[i][j]))
        return ret

