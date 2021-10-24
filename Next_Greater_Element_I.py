# 20211019
# LeetCode

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d, ms = dict(), list()
        for num in nums2[::-1]:
            while ms and num > ms[-1]: ms.pop()
            d[num] = -1 if not ms else ms[-1]
            ms.append(num)
        return [d[num] for num in nums1]

