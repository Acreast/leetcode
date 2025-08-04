# Last updated: 8/4/2025, 11:49:26 PM
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        res = 0
        total = 0
        basket = defaultdict(int)

        for r in range(len(fruits)):
            basket[fruits[r]] += 1
            total += 1
            
            while len(basket) > 2:
                f = fruits[l]
                basket[f] -= 1
                total -= 1
                l += 1
                if not basket[f]:
                    basket.pop(f)
            res = max(total, res)

        return res