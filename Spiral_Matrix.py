# 20210916
# LeetCode

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        d, didx = [[0, 1], [1, 0], [0, -1], [-1, 0]], 0
        m, n = len(matrix), len(matrix[0])
        v = [[0 for _ in range(n)] for _ in range(m)]
        i, j, ret = 0, 0, list()
        while len(ret) < m*n:
            v[i][j] = 1
            ret.append(matrix[i][j])
            i, j = i + d[didx][0], j + d[didx][1]
            if i < 0 or i >= m or j < 0 or j >= n or v[i][j] == 1:
                i, j = i - d[didx][0], j - d[didx][1]
                didx = (didx + 1)&3 # (didx + 1)%4
                i, j = i + d[didx][0], j + d[didx][1]
        return ret

