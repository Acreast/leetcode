# Last updated: 7/27/2025, 4:32:37 PM
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res = 0
        cleaned = [nums[0]]
        for num in nums[1:]:
            if num != cleaned[-1]:
                cleaned.append(num)

        for i in range(1, len(cleaned) - 1):
            if cleaned[i] > cleaned[i - 1] and cleaned[i] > cleaned[i + 1]:
                res += 1
            elif cleaned[i] < cleaned[i - 1] and cleaned[i] < cleaned[i + 1]:
                res += 1



        return res