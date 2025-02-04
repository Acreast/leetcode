class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in hash_map:
                hash_map.remove(s[l])
                l += 1
            hash_map.add(s[r])
            res = max(len(hash_map), res)
                                
        return res