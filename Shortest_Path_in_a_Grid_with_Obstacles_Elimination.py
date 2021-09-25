# 20210925
# LeetCode

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        bfs = [[[-1 for a in range(n)] for b in range(m)] for c in range(k + 1)]
        for i in range(k + 1): bfs[i][0][0] = 0
        q = [(0, 0, k),]
        while len(q) > 0:
            y, x, r = q.pop(0)
            if y == m - 1 and x == n - 1: return bfs[r][y][x]
            if y > 0:
                if grid[y - 1][x] == 0 and bfs[r][y - 1][x] == -1:
                    bfs[r][y - 1][x] = bfs[r][y][x] + 1
                    q.append((y - 1, x, r))
                elif r > 0 and grid[y - 1][x] != 0 and bfs[r - 1][y - 1][x] == -1:
                    bfs[r - 1][y - 1][x] = bfs[r][y][x] + 1
                    q.append((y - 1, x, r - 1))
            if y < m - 1:
                if grid[y + 1][x] == 0 and bfs[r][y + 1][x] == -1:
                    bfs[r][y + 1][x] = bfs[r][y][x] + 1
                    q.append((y + 1, x, r))
                elif r > 0 and grid[y + 1][x] != 0 and bfs[r - 1][y + 1][x] == -1:
                    bfs[r - 1][y + 1][x] = bfs[r][y][x] + 1
                    q.append((y + 1, x, r - 1))
            if x > 0:
                if grid[y][x - 1] == 0 and bfs[r][y][x - 1] == -1:
                    bfs[r][y][x - 1] = bfs[r][y][x] + 1
                    q.append((y, x - 1, r))
                elif r > 0 and grid[y][x - 1] != 0 and bfs[r - 1][y][x - 1] == -1:
                    bfs[r - 1][y][x - 1] = bfs[r][y][x] + 1
                    q.append((y, x - 1, r - 1))
            if x < n - 1:
                if grid[y][x + 1] == 0 and bfs[r][y][x + 1] == -1:
                    bfs[r][y][x + 1] = bfs[r][y][x] + 1
                    q.append((y, x + 1, r))
                elif r > 0 and grid[y][x + 1] != 0 and bfs[r - 1][y][x + 1] == -1:
                    bfs[r - 1][y][x + 1] = bfs[r][y][x] + 1
                    q.append((y, x + 1, r - 1))
        return -1

