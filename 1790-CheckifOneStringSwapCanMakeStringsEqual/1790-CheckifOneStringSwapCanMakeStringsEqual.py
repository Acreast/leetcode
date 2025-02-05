class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        first_diff_index = None
        second_diff_index = None
        diff_count = 0
        if len(s1) != len(s2):
            return False

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_count += 1
                if first_diff_index == None:
                    first_diff_index = i
                else:
                    second_diff_index = i
        
        if diff_count == 0:
            return True
        if diff_count > 2 or diff_count == 1:
            return False
        return s1[first_diff_index] == s2[second_diff_index] and s1[second_diff_index] == s2[first_diff_index]
