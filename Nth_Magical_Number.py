# 20211211
# LeetCode

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        gcd, tnum = a, b
        while tnum != 0: gcd, tnum = tnum, gcd%tnum
        lcm = (a*b)//gcd
        cand = sorted([a*i for i in range(1, lcm//a)] + [b*j for j in range(1, lcm//b + 1)])
        return (cand[(n - 1)%len(cand)] + lcm*((n - 1)//len(cand)))%1000000007

