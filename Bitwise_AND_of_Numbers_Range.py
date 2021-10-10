# 20211010
# LeetCode

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if len(bin(left)) != len(bin(right)): return 0
        lbits, rbits = bin(left)[2:], bin(right)[2:]
        ret = 0
        for i in range(len(lbits)):
            if lbits[i] != rbits[i]: break
            if lbits[i] == '1': ret |= 1<<(len(lbits) - 1 - i)
        return ret

