# 20211209
# LeetCode

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        ll = len(arr)
        v = [False]*len(arr)

        def jump(idx):
            nonlocal v, arr
            if arr[idx] == 0: return True
            v[idx] = True
            i1, i2 = idx - arr[idx], idx + arr[idx]
            res = False
            if i1 >= 0 and not v[i1]: res = jump(i1)
            if not res and i2 < len(arr) and not v[i2]: res = jump(i2)
            return res

        return jump(start)

