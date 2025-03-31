# Last updated: 3/31/2025, 11:23:55 AM
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}

        for i, n in enumerate(s):
            last_index[n] = i

        size, end = 0, 0
        res = []
        for i, c in enumerate(s):
            size += 1
            end = max(end, last_index[c])

            if i == end:
                res.append(size)
                size = 0

        return res