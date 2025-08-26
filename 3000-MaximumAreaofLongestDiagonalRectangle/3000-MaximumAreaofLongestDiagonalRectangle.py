# Last updated: 8/27/2025, 1:06:22 AM
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        longest = 0
        max_area = 0
        
        for length, width in dimensions:
            diag = math.sqrt(length * length + width * width)
            area = length * width
            
            if diag > longest:
                longest = diag
                max_area = area
            elif diag == longest:
                max_area = max(max_area, area)
        
        return max_area