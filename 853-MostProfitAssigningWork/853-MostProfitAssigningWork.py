# Last updated: 7/12/2025, 11:55:01 PM
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        max_difficulty = max(difficulty)
        max_profit_to_difficulty = [0] * (max_difficulty + 1)

        for d, p in zip(difficulty, profit):
            max_profit_to_difficulty[d] = max(max_profit_to_difficulty[d], p)
        
        for i in range(1, max_difficulty + 1):
            max_profit_to_difficulty[i] = max(max_profit_to_difficulty[i], max_profit_to_difficulty[i -1])

        total_profit = 0
        for ability in worker:
            if ability > max_difficulty:
                total_profit += max_profit_to_difficulty[max_difficulty]
            else:
                total_profit += max_profit_to_difficulty[ability]
            
        return total_profit