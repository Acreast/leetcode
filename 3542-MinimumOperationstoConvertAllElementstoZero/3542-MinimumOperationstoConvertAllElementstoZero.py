# Last updated: 11/11/2025, 12:07:44 AM
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        res = 0
        for n in nums:
            while stack and stack[-1] > n:
                stack.pop()
            if n == 0:
                continue
            if not stack or n != stack[-1]:
                res += 1
                stack.append(n)

        return res