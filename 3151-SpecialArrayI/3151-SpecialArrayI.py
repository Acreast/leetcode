class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        prev_flag = None
        for n in nums:
            cur = n % 2
            if prev_flag == None or prev_flag != cur:
                prev_flag = cur
                continue
            if prev_flag == cur:
                return False
        return True
            

