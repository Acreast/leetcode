# Last updated: 7/12/2025, 11:47:53 PM
class Solution(object):
    def maximumBeauty(self, items, queries):
        
        maxI = float('inf')
        res = [[0, 0, maxI]]
    
        items.sort(key=lambda x: x[0])

        for price, beauty in items:
            lastBracket = res[-1]
            if beauty > lastBracket[1]:
                res[-1][2] = price
                res.append([price, beauty, maxI])

        ans = []

        for x in queries:
            for i in range(len(res) - 1, -1, -1):
                if res[i][0] <= x:
                    ans.append(res[i][1])
                    break

        return ans