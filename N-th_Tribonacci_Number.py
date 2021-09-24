# 20210924
# LeetCode

class Solution:
    def __init__(self):
        self.tf = [0, 1, 1]

    def tribonacci(self, n: int) -> int:
        while len(self.tf) <= n: self.tf.append(self.tf[-1] + self.tf[-2] + self.tf[-3])
        return self.tf[n]

