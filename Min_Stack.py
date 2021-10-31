# 20211025
# LeetCode

class MinStack:

    def __init__(self):
        self.stack, self.minstack = list(), list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack) == 0 or val <= self.minstack[-1]: self.minstack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.minstack[-1]: self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
