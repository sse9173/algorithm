# 20210923
# LeetCode

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1: return ""
        half, changeF = len(palindrome)>>1, False
        for i in range(half):
            if palindrome[i] != 'a':
                palindrome = palindrome.replace(palindrome[i], 'a', 1)
                changeF = True
                break
        if changeF is False: palindrome = palindrome[:-1] + 'b'
        return palindrome

