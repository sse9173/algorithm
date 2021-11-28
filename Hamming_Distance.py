# 20211119
# LeetCode

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor, cnt = x^y, 0
        while xor != 0:
            cnt += xor&1
            xor >>= 1
        return cnt
