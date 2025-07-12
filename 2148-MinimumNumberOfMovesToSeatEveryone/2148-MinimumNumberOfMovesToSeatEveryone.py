# Last updated: 7/12/2025, 11:48:10 PM
class Solution:
    def minMovesToSeat(self, seats, students):
        pos = [0] * 101
        n = len(seats)
        for i in range(n):
            pos[seats[i]] += 1
            pos[students[i]] -= 1
        res = 0
        current = 0
        for i in pos:
            res += abs(current)
            current += i
        return res