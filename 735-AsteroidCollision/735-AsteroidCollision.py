# Last updated: 7/12/2025, 11:55:30 PM
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and a < 0 < stack[-1]:

                if abs(a) > stack[-1]:
                    stack.pop()

                elif abs(a) == stack[-1]:
                    stack.pop()
                    break
                
                else:
                    break
                
            else:
                stack.append(a)

        
        return stack