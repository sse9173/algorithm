# 20210616
# LeetCode

class Solution:
    def recurse(self, l, r, p):
        if l == 0 and r == 0:
            self.ret.append(p)
            return
        if l > 0: self.recurse(l - 1, r, p + '(')
        if r > 0 and l < r: self.recurse(l, r - 1, p + ')')
    def generateParenthesis(self, n: int) -> List[str]:
        self.ret = list()
        self.recurse(n, n, "")
        return self.ret
