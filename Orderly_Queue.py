# 20210905
# LeetCode

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            ret = s
            for i in range(len(s)):
                ret = min(ret, s[i:] + s[0:i])
            return ret
        else: return ''.join(sorted(s))

