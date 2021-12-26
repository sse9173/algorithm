# 20211217
# LeetCode

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(m): matrix[i][0] = int(matrix[i][0])
        for j in range(n): matrix[0][j] = int(matrix[0][j])
        ret = max(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] != 0:
                    matrix[i][j] = min(matrix[i][j - 1], matrix[i - 1][j - 1], matrix[i - 1][j]) + 1
            ret = max(ret, max(matrix[i]))
        return ret*ret

