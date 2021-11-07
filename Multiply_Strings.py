# 20211107
# LeetCode

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'
        res = [0 for _ in range(len(num1) + len(num2) + 1)]
        idx, tidx = 0, 0
        for c1 in num1[::-1]:
            tidx = idx
            for c2 in num2[::-1]:
                res[tidx] += int(c1)*int(c2)
                tidx += 1
            idx += 1
        for i in range(tidx - 1):
            if res[i] >= 10:
                res[i + 1] += res[i]//10
                res[i] %= 10
            res[i] = str(res[i])
        res = res[:tidx]
        res[-1] = str(res[-1])
        return ''.join(res[::-1])

