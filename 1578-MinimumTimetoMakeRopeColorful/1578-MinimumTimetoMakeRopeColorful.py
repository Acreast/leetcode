# Last updated: 11/3/2025, 11:33:40 PM
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l = 0
        res = 0 
        for r in range(1, len(colors)):
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    res += neededTime[l]
                    l = r
                else:
                    res += neededTime[r]
            else:
                l = r

        return res