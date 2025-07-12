# Last updated: 7/12/2025, 11:51:37 PM
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        my_dict = Counter(s)
        
        odd_count = 0
        for counter in my_dict.values():
            if counter % 2 != 0:
                odd_count += 1
        
        return odd_count <= k
