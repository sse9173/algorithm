# 20211108
# LeetCode

class Solution:
    def __init__(self):
        self.pool = [1, ]

    def numTrees(self, n: int) -> int:
        while len(self.pool) <= n:
            s, e = 0, len(self.pool) - 1
            val = 0
            while e >= 0:
                val += self.pool[s]*self.pool[e]
                s, e = s + 1, e - 1
            self.pool.append(val)
        return self.pool[n]

