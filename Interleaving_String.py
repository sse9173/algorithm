# 20210603
# LeetCode

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l1 + l2 != len(s3): return False
        if l1 == 0: return s2 == s3
        if l2 == 0: return s1 == s3
        l1 += 1
        l2 += 1
        dp = [[False for j in range(l2)] for i in range(l1)]
        dp[0][0] = True
        for i in range(1, l1): dp[i][0] = dp[i - 1][0] and (s1[i - 1] == s3[i - 1])
        for j in range(1, l2): dp[0][j] = dp[0][j - 1] and (s2[j - 1] == s3[j - 1])
        for i in range(1, l1):
            for j in range(1, l2):
                b1 = dp[i - 1][j] and (s1[i - 1] == s3[i + j - 1])
                b2 = dp[i][j - 1] and (s2[j - 1] == s3[i + j - 1])
                dp[i][j] = b1 or b2
        return dp[l1 - 1][l2 - 1]
