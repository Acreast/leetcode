# Last updated: 7/12/2025, 11:44:28 PM
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        index_map = {p:i for i, p in enumerate(positions)}

        stack = []

        for p in sorted(positions):
            i = index_map[p]

            if directions[i] == "R":
                stack.append(i)
            else:
                while stack and directions[stack[-1]] == "R" and healths[i]:
                    i2 = stack.pop()
                    if healths[i] > healths[i2]:
                        healths[i2] = 0
                        healths[i] -= 1
                    elif healths[i] < healths[i2]:
                        healths[i] = 0
                        healths[i2] -= 1
                        stack.append(i2)
                    else:
                        healths[i] = healths[i2] = 0
                    
                if healths[i]:
                    stack.append(i)
        
        return [h for h in healths if h > 0]