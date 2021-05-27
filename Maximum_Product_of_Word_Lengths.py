# 20210527
# LeetCode

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words.sort(key = len, reverse = True)
        bits = dict()
        ret = 0
        for i in range(len(words)):
            wl = len(words[i])
            if ret > wl*len(words[0]): break
            bit = 0
            for c in words[i]: bit |= 1<<(ord(c) - ord('a'))
            if bit in bits: continue
            for k, v in bits.items():
                if bit&k == 0:
                    cand = wl*v
                    if ret < cand: ret = cand
            bits[bit] = wl
        return ret
