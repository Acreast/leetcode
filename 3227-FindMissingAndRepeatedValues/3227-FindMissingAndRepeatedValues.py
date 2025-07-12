# Last updated: 7/12/2025, 11:43:40 PM
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        missing = 0
        dupe = 0
        seen = set()
        total_elem = len(grid) * len(grid[0])

        for row in grid:
            for elem in row:
                if elem in seen:
                    dupe = elem
                else:
                    seen.add(elem)

        for i in range(1, total_elem + 1):
            if i not in seen:
                missing = i
                break
        
        return [dupe,missing]
            