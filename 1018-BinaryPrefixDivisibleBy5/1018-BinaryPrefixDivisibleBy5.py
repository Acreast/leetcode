# Last updated: 11/24/2025, 1:21:41 PM
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        binary_string = ""
        for n in nums:
            binary_string += str(n)
            binary_number = int(binary_string, 2)
            if binary_number % 5 == 0:
                res.append(True)
            else:
                res.append(False)

        return res