# 20211210
# LeetCode

class Solution:
    def numTilings(self, n: int) -> int:
        domino = [1, 2] + [0,]*n
        tromino = [1]*n
        for i in range(2, n):
            domino[i] = (domino[i - 1] + domino[i - 2] + tromino[i - 1]*2)%1000000007
            tromino[i] = (domino[i - 2] + tromino[i - 1])%1000000007
        return domino[n - 1]
