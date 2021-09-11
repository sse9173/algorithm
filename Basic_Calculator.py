# 20210911
# LeetCode

class Solution:
    def calculate(self, s: str) -> int:
        stack = list()
        for c in s:
            if c == ' ': continue
            elif c == ')':
                rstack = list()
                while stack[-1] != '(': rstack.append(stack.pop())
                stack.pop() # pop '('
                while len(rstack) > 1:
                    n1, op, n2 = rstack.pop(), rstack.pop(), rstack.pop()
                    rstack.append(n1 + n2 if op == '+' else n1 - n2)
                stack.append(rstack[0])
            elif c not in ['(', '+', '-']:
                if len(stack) > 0 and stack[-1] not in ['(', '+', '-']:
                    stack[-1] = stack[-1]*10 + int(c)
                else: stack.append(int(c))
            else: stack.append(c)
        ret = stack[0] if stack[0] != '-' else -stack[1]
        for i in range(1 if stack[0] != '-' else 2, len(stack), 2):
            op, n2 = stack[i], stack[i + 1]
            ret = ret + n2 if op == '+' else ret - n2
        return ret

