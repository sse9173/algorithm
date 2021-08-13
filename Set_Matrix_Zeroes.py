# 20210813
# LeetCode

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows, cols = list(), list()
        zeroes = list()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i not in rows: rows.append(i)
                    if j not in cols: cols.append(j)
        for row in rows: matrix[row] = [0,]*n
        for col in cols:
            for i in range(m): matrix[i][col] = 0
