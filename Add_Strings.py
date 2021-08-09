# 20210809
# LeetCode

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ret = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 and j >= 0:
            digit = int(num1[i]) + int(num2[j]) + carry
            if digit >= 10:
                digit -= 10
                carry = 1
            else: carry = 0
            ret = str(digit) + ret
            i -= 1
            j -= 1
        while i >= 0:
            digit = int(num1[i]) + carry
            if digit >= 10:
                digit -= 10
                carry = 1
            else: carry = 0
            ret = str(digit) + ret
            i -= 1
        while j >= 0:
            digit = int(num2[j]) + carry
            if digit >= 10:
                digit -= 10
                carry = 1
            else: carry = 0
            ret = str(digit) + ret
            j -= 1
        return ret if carry == 0 else "1" + ret
