# Last updated: 7/12/2025, 11:42:53 PM
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # last_consecutive_index
        lci = 0
        res = []
        sub_arr_size = 1
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1] + 1:
                sub_arr_size += 1
            
            if i - lci + 1 > k:
                if nums[lci] + 1 == nums[lci + 1]:
                    sub_arr_size -= 1
                lci += 1
            
            if i - lci + 1 == k:
                if sub_arr_size == k:
                    res.append(nums[i])
                else:
                    res.append(-1)

        return res
