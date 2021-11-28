# 20211127
# LeetCode

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = [1,]*len(nums), [1,]*len(nums)
        for i in range(1, len(nums)):
            pre[i] = pre[i - 1]*nums[i - 1]
            post[-i - 1] = post[-i]*nums[-i]
        ret = list()
        for i in range(len(nums)): ret.append(pre[i]*post[i])
        return ret

