# 20211029
# LeetCode

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rotten, fresh = list(), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2: rotten.append((i, j))
                elif grid[i][j] == 1: fresh += 1
        if len(rotten) == 0: return 0 if fresh == 0 else -1
        minutes = 0
        while len(rotten) > 0:
            minutes += 1
            newrotten = list()
            for y, x in rotten:
                if y > 0 and grid[y - 1][x] == 1:
                    grid[y - 1][x] = 2
                    newrotten.append((y - 1, x))
                    fresh -= 1
                if x < n - 1 and grid[y][x + 1] == 1:
                    grid[y][x + 1] = 2
                    newrotten.append((y, x + 1))
                    fresh -= 1
                if y < m - 1 and grid[y + 1][x] == 1:
                    grid[y + 1][x] = 2
                    newrotten.append((y + 1, x))
                    fresh -= 1
                if x > 0 and grid[y][x - 1] == 1:
                    grid[y][x - 1] = 2
                    newrotten.append((y, x - 1))
                    fresh -= 1
            rotten = newrotten
        return -1 if fresh > 0 else minutes - 1

