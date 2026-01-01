# Last updated: 1/1/2026, 3:24:27 PM
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        carry = 1
4        for i in range(len(digits) -1, -1, -1):
5            sum = digits[i] + carry
6            digits[i] = sum % 10
7            carry = sum // 10
8        if carry:
9            digits = [1] + digits
10
11        return digits 