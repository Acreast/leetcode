# Last updated: 7/12/2025, 11:47:36 PM
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        stack_locked = []
        stack_notlocked = []


        for i in range(len(s)):
            if locked[i] == "0":
                stack_notlocked.append(i)
            elif s[i] == "(":
                stack_locked.append(i)
            else:
                if stack_locked:
                    stack_locked.pop()
                elif stack_notlocked:
                    stack_notlocked.pop()
                else:
                    return False
        
        while stack_locked and stack_notlocked and stack_locked[-1] < stack_notlocked[-1]:
            stack_locked.pop()
            stack_notlocked.pop()
        if stack_locked:
            return False
        return True if len(s) % 2 == 0 else False

