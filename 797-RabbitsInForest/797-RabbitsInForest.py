# Last updated: 7/12/2025, 11:55:15 PM
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbit_says = Counter(answers)
        total = 0
        for quote in rabbit_says:
            total += ceil(float(rabbit_says[quote])/ (quote + 1)) * (quote + 1)
        return int(total)