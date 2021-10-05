# 20211005
# LeetCode

class Solution:
    def __init__(self):
        self.pool = [0, 1, 2]

    def climbStairs(self, n: int) -> int:
        while len(self.pool) <= n: self.pool.append(self.pool[-1] + self.pool[-2])
        return self.pool[n]
