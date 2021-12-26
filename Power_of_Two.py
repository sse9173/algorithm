# 20211221
# LeetCode

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return False if n <= 0 else not bool(n&(n - 1))

