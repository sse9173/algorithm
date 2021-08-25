# 20210825
# LeetCode

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c <= 2: return True  # 0 = 0 + 0, 1 = 1 + 0, 2 = 1 + 1
        a, b = 0, int(math.sqrt(c))
        while a <= b:
            tc = a*a + b*b
            if tc == c: return True
            if tc < c: a += 1
            else: b -= 1
        return False
