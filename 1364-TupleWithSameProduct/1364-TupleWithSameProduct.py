# Last updated: 7/12/2025, 11:52:22 PM
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_cnt = defaultdict(int)
        pair_cnt = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                pair_cnt[product] += product_cnt[product]
                product_cnt[product] += 1
        
        res = 0
        for cnt in pair_cnt.values():
            res += 8 * cnt
        
        return res