# Last updated: 7/12/2025, 11:45:27 PM
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = 0
            k -= map[nums[i]]
            map[nums[i]] += 1
            while k <= 0:
                map[nums[left]] -= 1
                k += map[nums[left]]
                left += 1
            count += left
        return count