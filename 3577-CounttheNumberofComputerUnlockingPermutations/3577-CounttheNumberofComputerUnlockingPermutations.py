# Last updated: 12/10/2025, 1:32:05 PM
1class Solution:
2    def countPermutations(self, complexity: List[int]) -> int:
3        if complexity[0] >= min(complexity[1:]):
4            return 0
5        
6        return factorial(len(complexity) - 1) % (10 ** 9 + 7)