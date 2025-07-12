# Last updated: 7/12/2025, 11:47:40 PM
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        is_even = set()
        n = len(digits)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or j == k or k == i:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if num >= 100 and num % 2 == 0:
                        is_even.add(num)

        return sorted(list(is_even))