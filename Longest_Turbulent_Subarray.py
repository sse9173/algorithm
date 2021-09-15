# 20210915
# LeetCode

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1: return 1
        if len(arr) == 2: return 2 if arr[0] != arr[1] else 1
        prev = -1 if arr[0] > arr[1] else 0 if arr[0] == arr[1] else 1
        ret = ll = 1 if arr[0] == arr[1] else 2
        for i in range(2, len(arr)):
            if ret > ll + (len(arr) - i): break
            if arr[i - 1] < arr[i]:
                ll = (ll + 1) if prev == -1 else 2
                prev = 1
            elif arr[i - 1] == arr[i]:
                ll, prev = 1, 0
            elif arr[i - 1] > arr[i]:
                ll = (ll + 1) if prev == 1 else 2
                prev = -1
            if ret < ll: ret = ll
        return ret

