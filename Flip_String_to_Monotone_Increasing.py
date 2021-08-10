# 20210810
# LeetCode

# Very Slow (188ms)
# Any Other Faster Way ?

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flip, cnt1 = 0, 0
        for d in s:
            if d == '1': cnt1 += 1
            elif cnt1 != 0: flip += 1
            flip = min(flip, cnt1)
        return flip
