# 20211030
# LeetCode

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        ret = ""
        j = 1
        for i in range(len(s)):
            cand = s[i:i + j]
            pool = s[i + 1:]
            while cand in pool:
                ret = cand
                j += 1
                cand = s[i:i + j]
        return ret

