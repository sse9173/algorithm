# 20210520
# LeetCode

class Solution:
    def maximumGap(self, nums: List[int]) -> int:   # 52ms
        if len(nums) < 2: return 0
        nums.sort()
        ret = 0
        for i in range(1, len(nums)):
            tmp = nums[i] - nums[i - 1]
            if ret < tmp: ret = tmp
        return ret
    """
    def maximumGap(self, nums: List[int]) -> int:   # 60ms
        if len(nums) < 2: return 0
        maxNum = max(nums)
        minNum = min(nums)
        step = (maxNum - minNum)//(len(nums) - 1)
        if step == 0: step = 1
        buckets = [list() for i in range(((maxNum - minNum)//step) + 1)]
        for num in nums: buckets[(num - minNum)//step].append(num)
        ret = 0
        curmax = 0
        for bucket in buckets:
            if len(bucket) == 0: continue
            prevmax = bucket[0] if curmax == 0 else curmax
            curmin = bucket[0]
            for num in bucket:
                if curmin > num: curmin = num
                if curmax < num: curmax = num
            locAns = curmin - prevmax
            if ret < locAns: ret = locAns
        return ret
    """
