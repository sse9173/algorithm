# 20210527
# LeetCode

import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = list()
        for token in tokens:
            if token == '+': nums.append(nums.pop() + nums.pop())
            elif token == '-': nums.append(-nums.pop() + nums.pop())
            elif token == '*': nums.append(nums.pop()*nums.pop())
            elif token == '/':
                n2 = nums.pop()
                n1 = nums.pop()
                num = n1/n2
                if num < 0: nums.append(math.ceil(num))
                else: nums.append(math.floor(num))
            else:   # integer token
                nums.append(int(token))
        return nums[0]
