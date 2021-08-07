# 20210807
# LeetCode

class Solution:
    def minCut(self, s: str) -> int:
        if len(s) == 1: return 0
        cut = [i for i in range(len(s))]
        for i in range(1, len(s)):
            for j in range(0, len(s) - i):
                if i - j < 0 or s[i - j] !=s[i + j]: break
                cut[i + j] = 0 if i - j == 0 else min(cut[i + j], cut[i - j - 1] + 1)
            for j in range(0, len(s) - i):
                if i - j - 1 < 0 or s[i - j - 1] != s[i + j]: break
                cut[i + j] = 0 if i - j - 1 == 0 else min(cut[i + j], cut[i - j - 2] + 1)
        return cut[-1]

