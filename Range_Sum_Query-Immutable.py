# 20210816
# LeetCode

class NumArray:
    def __init__(self, nums: List[int]):
        self.sums = nums[:]
        for i in range(1, len(nums)): self.sums[i] += self.sums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right] if left == 0 else self.sums[right] - self.sums[left - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
