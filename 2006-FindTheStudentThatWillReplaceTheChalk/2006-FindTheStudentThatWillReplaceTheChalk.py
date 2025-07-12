# Last updated: 7/12/2025, 11:48:49 PM
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_required_chalk = sum(chalk)
        remainder = k % total_required_chalk
        
        for i, usage in enumerate(chalk):
            if remainder < usage:
                return i
            remainder -= usage
            
        return 0
