# Last updated: 4/6/2025, 9:31:06 PM
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        cache = {}
        def dfs(i):
            if i == len(nums):
                return []
            if i in cache:
                return cache[i]
            res = [nums[i]]
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    temp = [nums[i]] + dfs(j)
                    if len(temp) > len(res):
                        res = temp
            cache[i] = res
            return res
        
        result = []
        for i in range(len(nums)):
            temp_res = dfs(i)
            if len(temp_res) > len(result):
                result = temp_res
        
        return result