# 20211022
# LeetCode

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = dict()
        for c in s:
            if c not in freq: freq[c] = 1
            else: freq[c] += 1
        freq = sorted(freq.items(), key = (lambda x: x[1]), reverse = True)
        ret = ''
        for c, cnt in freq: ret += c*cnt
        return ret
