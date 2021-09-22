# 20210922
# LeetCode

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ret, dp = 0, [0, ]
        for s in arr:
            bits, dup = 0, 0
            for c in s:
                i = 1<<(ord(c) - ord('a'))
                if i&bits != 0:
                    dup = 1
                    break
                bits |= i
            if dup == 1: continue
            for elem in dp:
                if bits&elem != 0: continue
                dp.append(bits|elem)
                ret = max(ret, bin(dp[-1]).count('1'))
        return ret
