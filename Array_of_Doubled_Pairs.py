# 20210811
# LeetCode

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        if len(arr) == 0: return True
        d = dict()
        for num in arr:
            if num not in d: d[num] = 0
            d[num] += 1
        aset = sorted(list(set(arr)), key = abs)
        if aset[0] == 0:
            if d[0]%2 != 0: return False
            del d[0]
            del aset[0]
        for num in aset:
            if len(d) == 0: return True
            if num not in d: continue
            dnum = num*2
            if dnum not in d: return False
            d[dnum] -= d[num]
            if d[dnum] < 0: return False
            elif d[dnum] == 0: del d[dnum]
            del d[num]
        return True

