# Last updated: 9/17/2025, 11:01:21 PM
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pair,reverse=True):
            stack.append((target - p) / s)
            if len(stack) >= 2:
                if stack[-1] <= stack[-2]:
                    stack.pop()
        
        return len(stack)
            
