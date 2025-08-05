# Last updated: 8/5/2025, 11:24:16 PM
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        occupied = set()
        for fruit in fruits:
            for i in range(len(baskets)):
                if i in occupied:
                    continue
                if fruit <= baskets[i]:
                    occupied.add(i)
                    break
            
        return len(baskets) - len(occupied) 