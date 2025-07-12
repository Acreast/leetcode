# Last updated: 7/12/2025, 11:49:13 PM
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        if s1 == s2:
            return True
        
        diff_indexes = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_indexes.append(i)
        if len(diff_indexes) != 2:
            return False
            
        if s1[diff_indexes[0]] == s2[diff_indexes[1]] and s2[diff_indexes[0]] == s1[diff_indexes[1]]:
            return True

        return False
