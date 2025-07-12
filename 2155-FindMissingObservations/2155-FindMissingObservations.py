# Last updated: 7/12/2025, 11:48:04 PM
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_sum = mean * (m+n)
        missing_sum = total_sum - sum(rolls)

        if missing_sum > 6 * n or missing_sum < n:
            return []
        
        result = []

        while n:
            dice = min(6, missing_sum - n + 1)
            result.append(dice)
            missing_sum -= dice
            n -= 1
        
        return result