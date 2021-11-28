# 20211116
# Leetcode

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def compare(num):
            nonlocal m, n, k
            cnt = 0
            for i in range(1, m + 1):
                cnt += min(n, num//i)
            return cnt >= k

        s, e = 1, m*n
        while s < e:
            mid = (s + e)>>1
            if compare(mid) is True: e = mid
            else: s = mid + 1
        return s

