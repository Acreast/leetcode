# Last updated: 3/31/2025, 3:25:11 PM
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}

        end, size = 0, 0
        res = []

        for i, c in enumerate(s):
            last_index[c] = i
        
        for i, c in enumerate(s):
            size += 1
            end = max(end, last_index[c])
            if i == end:
                res.append(size)
                size = 0
        return res