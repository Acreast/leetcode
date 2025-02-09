class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        total_pairs = 0
        counter = defaultdict(int)

        for i in range(len(nums)):
            total_pairs += i
            good_pairs += counter[nums[i] - i]
            counter[nums[i]- i] += 1

        return total_pairs - good_pairs