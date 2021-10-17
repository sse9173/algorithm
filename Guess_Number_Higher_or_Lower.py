# 20211012
# LeetCode

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        s, e = 1, n
        while s <= e:
            num = (s + e)>>1
            res = guess(num)
            if res == 0: return num
            elif res < 0: e = num - 1
            else: s = num + 1

