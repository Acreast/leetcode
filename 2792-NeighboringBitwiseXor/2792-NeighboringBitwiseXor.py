# Last updated: 7/12/2025, 11:44:39 PM
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        first = 0
        last = 0
        for n in derived:
            if n:
                last = ~last

        return first == last