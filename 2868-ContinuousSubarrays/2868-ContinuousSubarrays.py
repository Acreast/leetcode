# Last updated: 7/12/2025, 11:44:25 PM
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        l, res = 0, 0
        minD, maxD = deque(), deque()
        
        for r in range(len(nums)):
            while minD and nums[minD[-1]] >= nums[r]: minD.pop()
            while maxD and nums[maxD[-1]] <= nums[r]: maxD.pop()
            minD.append(r)
            maxD.append(r)
            
            while nums[maxD[0]] - nums[minD[0]] > 2:
                l += 1
                if minD[0] < l: minD.popleft()
                if maxD[0] < l: maxD.popleft()
            
            res += r - l + 1
        
        return res