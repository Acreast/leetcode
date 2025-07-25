# Last updated: 7/12/2025, 11:44:57 PM
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = defaultdict(int)
        res = []

        for n in nums:
            row = count[n]
            if len(res) == row:
                res.append([])

            res[row].append(n)
            count[n] += 1

        return res