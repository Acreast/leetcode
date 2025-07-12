# Last updated: 7/12/2025, 11:45:37 PM
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        mp = {}
        nums.sort()
        res = -1

        for num in nums:
            sqrt = isqrt(num)

            if sqrt * sqrt == num and sqrt in mp:
                mp[num] = mp[sqrt] + 1
                res = max(res, mp[num])
            else:
                mp[num] = 1
                
        return res