# 20211220
# LeetCode

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ret = [[arr[0], arr[1]],]
        mindiff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] < mindiff:
                ret = [[arr[i - 1], arr[i]], ]
                mindiff = arr[i] - arr[i - 1]
            elif arr[i] - arr[i - 1] == mindiff:
                ret.append([arr[i - 1], arr[i]])
        return ret
