# 20211213
# LeetCode

class Solution:
    def maxPower(self, s: str) -> int:
        power = [1 for _ in range(len(s))]
        ret = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                power[i] += power[i - 1]
                ret = max(ret, power[i])
        return ret
