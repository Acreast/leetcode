# Last updated: 10/20/2025, 8:28:39 PM
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for op in operations:
            if op == "--X" or op == "X--":
                res -= 1
            else:
                res += 1

        return res