# Last updated: 7/12/2025, 11:47:22 PM
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        cache = [0] * len(questions)
        def backtrack(i):
            if i >= len(questions):
                return 0
            if cache[i]:
                return cache[i]
            
            points, brainpower = questions[i]
            cache[i] = max(
                backtrack(i + 1),
                points + backtrack(i + brainpower + 1)
            )
            return cache[i]
        

        return backtrack(0)