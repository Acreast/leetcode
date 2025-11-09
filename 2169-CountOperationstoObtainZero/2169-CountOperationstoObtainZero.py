# Last updated: 11/9/2025, 11:17:29 PM
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        while num1 > 0 and num2 > 0:
            count += 1
            if num1 <= num2:
                num2 -= num1
            else:
                num1 -= num2

        return count