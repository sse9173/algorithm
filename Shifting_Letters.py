# 20210908
# LeetCode

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shifts[-1] %= 26
        num = ord(s[-1]) + shifts[-1]
        ret = chr(num if num <= ord('z') else num - ord('z') + ord('a') - 1)
        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] = (shifts[i] + shifts[i + 1])%26
            num = ord(s[i]) + shifts[i]
            ret += chr(num if num <= ord('z') else num - ord('z') + ord('a') - 1)
        return ret[::-1]

