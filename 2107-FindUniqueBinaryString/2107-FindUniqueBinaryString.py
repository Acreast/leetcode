# Last updated: 7/12/2025, 11:48:19 PM
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        str_set = {s for s in nums}

        def backtrack(i, cur):
            if i == len(nums):
                res = "".join(cur)
                return None if res in str_set else res
            
            res = backtrack(i + 1, cur)
            if res: return res

            cur[i] = "1"
            res = backtrack(i + 1, cur)
            if re: return res

        return backtrack(0, ["0" for s in nums])