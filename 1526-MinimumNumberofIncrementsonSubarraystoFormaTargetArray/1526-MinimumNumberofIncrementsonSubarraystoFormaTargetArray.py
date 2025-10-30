# Last updated: 10/30/2025, 11:44:58 PM
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                res += target[i] -  target[i - 1]

        return res