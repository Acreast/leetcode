# Last updated: 9/7/2025, 4:55:12 PM
class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        if n % 2:
            res = [0]

        for num in range(1, n//2 + 1):
            res.append(num)
            res.append(-num)
        
        return res