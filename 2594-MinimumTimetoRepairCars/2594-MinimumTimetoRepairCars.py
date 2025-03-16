class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def repair_counter(time):
            count = 0
            for r in ranks:
                count += int(sqrt(time / r))
            return count

        l, r = 1, ranks[0] * cars *cars
        res = -1
        while l <= r:
            m = (l + r) // 2
            repair_count = repair_counter(m)
            if repair_count >= cars:
                res = m
                r = m - 1
            else:
                l = m + 1

        return res