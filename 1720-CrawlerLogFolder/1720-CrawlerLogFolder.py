# Last updated: 7/12/2025, 11:50:18 PM
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                res = max(0, res - 1)
            else :
                res += 1
        return res