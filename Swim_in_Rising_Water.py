# 20210620
# LeetCode

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, pq, ret = len(grid), list(), grid[0][0]
        heappush(pq, grid[0][0]<<12)
        while len(pq) != 0:
            item = heappop(pq)
            lvl, y, x = item>>12, (item>>6)&63, item&63
            ret = max(ret, lvl)
            if y == n - 1 and x == n - 1: break
            if y - 1 >= 0 and grid[y - 1][x] < 2500:
                heappush(pq, (grid[y - 1][x]<<12)|((y - 1)<<6)|x)
                grid[y - 1][x] = 2500
            if y + 1 < n and grid[y + 1][x] < 2500:
                heappush(pq, (grid[y + 1][x]<<12)|((y + 1)<<6)|x)
                grid[y + 1][x] = 2500
            if x - 1 >= 0 and grid[y][x - 1] < 2500:
                heappush(pq, (grid[y][x - 1]<<12)|(y<<6)|(x - 1))
                grid[y][x - 1] = 2500
            if x + 1 < n and grid[y][x + 1] < 2500:
                heappush(pq, (grid[y][x + 1]<<12)|(y<<6)|(x + 1))
                grid[y][x + 1] = 2500
        return ret

