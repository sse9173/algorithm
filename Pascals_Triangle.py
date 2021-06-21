# 20210621
# LeetCode

class Solution:
    triangle = [[1], [1, 1]]
    for i in range(1, 30):
        row = [1, ]
        for j in range(len(triangle[i]) - 1):
            row.append(triangle[i][j] + triangle[i][j + 1])
        triangle.append(row + [1,])

    def generate(self, numRows: int) -> List[List[int]]:
        return self.triangle[:numRows]

