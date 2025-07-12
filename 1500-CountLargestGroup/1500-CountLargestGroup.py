# Last updated: 7/12/2025, 11:51:39 PM
class Solution:
    def countLargestGroup(self, n: int) -> int:
        def digit_sum(num):
            return sum(int(d) for d in str(num))
        
        count_map = {}
        max_size = 0

        for i in range(1, n + 1):
            s = digit_sum(i)
            count_map[s] = count_map.get(s, 0) + 1
            if count_map[s] > max_size:
                max_size = count_map[s]
        
        return sum(1 for size in count_map.values() if size == max_size)