# Last updated: 7/12/2025, 11:44:14 PM
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count = 0
        equals = 0
        hash = defaultdict(int)
        hash[0] = 1

        for i in nums:
            if i % modulo == k:
                equals += 1
            rem = equals % modulo
            needed = (rem - k + modulo) % modulo
            count += hash[needed]
            hash[rem] += 1
        return count