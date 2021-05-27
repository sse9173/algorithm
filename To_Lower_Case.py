# 20210523
# LeetCode

class Solution:
    def toLowerCase(self, s: str) -> str:   # 20ms
        ret = ""
        for c in s:
            if c.isupper(): ret += c.lower()
            else: ret += c
        return ret

    """
    def toLowerCase(self, s: str) -> str:   # 32ms
        return s.lower()
    """
