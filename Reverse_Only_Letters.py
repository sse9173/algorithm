# 20210914
# LeetCode

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        f, t = 0, len(s) - 1
        ret = list(s)
        while f < t:
            while f < t and not('a' <= ret[f] <= 'z') and not('A' <= ret[f] <= 'Z'): f += 1
            while f < t and not('a' <= ret[t] <= 'z') and not('A' <= ret[t] <= 'Z'): t -= 1
            ret[f], ret[t] = ret[t], ret[f]
            f, t = f + 1, t - 1
        return ''.join(ret)

