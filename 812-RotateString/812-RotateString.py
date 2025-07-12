# Last updated: 7/12/2025, 11:55:10 PM
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in s + s